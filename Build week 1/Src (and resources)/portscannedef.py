import socket
import threading
import ipaddress
import os
from queue import Queue
from colorama import Fore, Style


def check_port_tcp(ip, port, output_queue):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        s.close()
        output_queue.put((port, 'TCP', True))
    except:
        output_queue.put((port, 'TCP', False))

def check_port_udp(ip, port, output_queue):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        s.sendto(b'', (ip, port))
        response, _ = s.recvfrom(1024)
        if response:
            output_queue.put((port, 'UDP', True))
        else:
            output_queue.put((port, 'UDP', False))
    except:
        output_queue.put((port, 'UDP', False))

def scan_ports(ip, lowport, highport):
    # Default language is English
    language = 'ENG'

    # Check if config.py exists
    if os.path.exists('config.py'):
        from config import LANGUAGE
        language = LANGUAGE

    output_queue = Queue()

    if language == 'ITA':
        print(f"Sto scannerizzando l'host {ip} dalle porte {lowport} alla {highport}:")
    elif language == 'ENG':
        print(f"Scanning host {ip} from port {lowport} to {highport}:")

    threads = []
    for port in range(lowport, highport + 1):
        tcp_thread = threading.Thread(target=check_port_tcp, args=(ip, port, output_queue))
        udp_thread = threading.Thread(target=check_port_udp, args=(ip, port, output_queue))
        threads.extend([tcp_thread, udp_thread])
        tcp_thread.start()
        udp_thread.start()

    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        if language == 'ITA':
            print("\nInterruzione richiesta. Terminazione in corso...")
        elif language == 'ENG':
            print("\nInterrupt requested. Terminating...")

    results = []
    while not output_queue.empty():
        results.append(output_queue.get())

    results.sort()  # Ordina i risultati per numero di porta
    printed_ports = set()  # Set per tenere traccia delle porte già stampate
    for port, protocol, status in results:
        if port not in printed_ports:  # Controlla se la porta è già stata stampata
            if language == 'ITA':
                tcp_status = f"{Fore.GREEN}APERTA{Style.RESET_ALL}" if protocol == 'TCP' and status else f"{Fore.RED}CHIUSA{Style.RESET_ALL}"
                udp_status = f"{Fore.GREEN}APERTA{Style.RESET_ALL}" if protocol == 'UDP' and status else f"{Fore.RED}CHIUSA{Style.RESET_ALL}"
                print(f"Porta {port} - UDP [{udp_status}] - TCP [{tcp_status}]")
            elif language == 'ENG':
                tcp_status = f"{Fore.GREEN}OPEN{Style.RESET_ALL}" if protocol == 'TCP' and status else f"{Fore.RED}CLOSED{Style.RESET_ALL}"
                udp_status = f"{Fore.GREEN}OPEN{Style.RESET_ALL}" if protocol == 'UDP' and status else f"{Fore.RED}CLOSED{Style.RESET_ALL}"
                print(f"Port {port} - UDP [{udp_status}] - TCP [{tcp_status}]")
            printed_ports.add(port)  # Aggiunge la porta al set delle porte stampate

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def get_valid_ip():
    # Default language is English
    language = 'ENG'

    # Check if config.py exists
    if os.path.exists('config.py'):
        from config import LANGUAGE
        language = LANGUAGE

    while True:
        if language == 'ENG':
            ip = input("Enter the IP address: ")
            if validate_ip(ip):
                return ip
            else:
                print("Invalid IP address format. Please try again.")
        elif language == 'ITA':
            ip = input("Inserisci l'indirizzo IP: ")
            if validate_ip(ip):
                return ip
            else:
                print("Formato dell'indirizzo IP non valido. Riprova.")
        else:
            print("Unsupported language. Using English as default.")
            ip = input("Enter the IP address: ")
            if validate_ip(ip):
                return ip
            else:
                print("Invalid IP address format. Please try again.")
            
def validate_port_range(port_range):
    try:
        start, end = map(int, port_range.split('-'))
        if not (0 < start <= end <= 65535):  # Controlla che sia nell'intervallo desiderato
            return False
        return True
    except ValueError:
        return False

def get_valid_port_range(language):
    while True:
        if language == 'ENG':
            port_range = input("Enter the port range (format ex: 1-65535): ")
            error_message = "Invalid port range. Please try again."
        elif language == 'ITA':
            port_range = input("Inserisci l'intervallo di porte (formato es: 1-65535): ")
            error_message = "Intervallo di porte non valido. Riprova."
        
        if validate_port_range(port_range):
            return port_range
        else:
            print(error_message)