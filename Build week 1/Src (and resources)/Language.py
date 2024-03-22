import Port_scanner 
import Verbi
import opener
import DVWA
import phpmyadmin
import os
from colorama import Fore

def get_menu_ITA():
    print(Fore.WHITE+
        "[1] Port scanner\n"
        "[2] Phpmyadmin  \n"
        "[3] DVWA\n"
        "[4] Verbi HTTP\n"
        "[5] Visualizzazione schema packet tracer\n"
        "[6] Visualizzazione documentazione\n"
        "[7] Apri il preventivo\n"
        "[8] Apri report phpmyadmin\n"
        "[9] Apri report dvwa\n"
        "[10] Ricarica il menu'\n"
        "[11] Seleziona lingua\n"
        "[12] Uscita\n")

def get_menu_ENG():
    print(Fore.WHITE +
        "[1] Port scanner\n"
        "[2] Phpmyadmin\n" 
        "[3] DVWA\n" 
        "[4] HTTP verbs \n"
        "[5] View packet tracer schema\n" 
        "[6] View documentation\n" 
        "[7] Open preventive\n" 
        "[8] Open phpmyadmin's report\n"
        "[9] OPen DVWA's report \n"
        "[10] Reload the menu' \n"
        "[11] Select language \n"
        "[12] Exit\n")

def start_ITA():
    from config import LANGUAGE
    while True:
        choice =input("Inserire l'opzione desiderata: ")
        if choice == '1':
            ip = Port_scanner.get_valid_ip()
            portrange = Port_scanner.get_valid_port_range(LANGUAGE)
            lowport, highport = map(int, portrange.split('-'))
            Port_scanner.scan_ports(ip, lowport, highport)

        elif choice == '2':
            phpmyadmin.phpMyAdmin()
            get_menu_ITA()

        elif choice == '3':
            DVWA.print_dvwa_menu()
            DVWA.start_ITA()
            get_menu()

        elif choice == '4':
            url = input("Inserire l'URL da vreificare: ")
            supported_verbs = Verbi.check_http_verbs(url)

            if supported_verbs:
                verbs_string = ", ".join([f"{Fore.GREEN}[{verb}]{Fore.RESET}" for verb in supported_verbs])
                print(f"Verbi HTTP supportati per {url}: {verbs_string}")
            else:
                print(f"Nessun verbo HTTP supportato per {url}")
        
        elif choice == '5':
            opener.open_png_image()

        elif choice == '6':
            opener.open_pdf_based_on_language()

        elif choice == '7':
            opener.open_preventivo_based_on_language()
        
        elif choice == '8':
            opener.open_report_phpmyadmin_based_on_language()
        
        elif choice == '9':
            opener.open_report_dvwa_based_on_language()

        elif choice == '10':
            get_menu_ITA()

        elif choice == '11':
            Select_language()
            break

        elif choice == '12':
            print("Arrivederci!")
            break

        else:
            print("Opzione non trovata\n")
        
        

def start_ENG():
    from config import LANGUAGE
    while True:
        choice = input("Enter the desired option: ")
        if choice == '1':
            ip = Port_scanner.get_valid_ip()
            portrange = Port_scanner.get_valid_port_range(LANGUAGE)
            lowport, highport = map(int, portrange.split('-'))
            Port_scanner.scan_ports(ip, lowport, highport)

        elif choice == '2':
            phpmyadmin.phpMyAdmin()
            get_menu_ENG()

        elif choice == '3':
            DVWA.print_dvwa_menu_ENG()
            DVWA.start_ENG()
            get_menu()

        elif choice == '4':
            url = input("Enter the URL to check: ")
            supported_verbs = Verbi.check_http_verbs(url)

            if supported_verbs:
                verbs_string = ", ".join([f"{Fore.GREEN}[{verb}]{Fore.RESET}" for verb in supported_verbs])
                print(f"Supported HTTP verbs for {url}: {verbs_string}")
            else:
                print(f"No supported HTTP verbs found for {url}")

        elif choice == '5':
            opener.open_png_image()
        
        elif choice == '6':
            opener.open_pdf_based_on_language()

        elif choice == '7':
            opener.open_preventivo_based_on_language()
        
        elif choice == '8':
            opener.open_report_phpmyadmin_based_on_language()
        
        elif choice == '9':
            opener.open_report_dvwa_based_on_language()

        elif choice == '10':
            get_menu_ENG()

        elif choice == '11':
            Select_language()
            break
            
        elif choice == '12':
            print("See you soon!")
            break

        else:
            print("Option not found \n")

def get_menu():
    config_file = 'config.py'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('LANGUAGE'):
                    language = line.split('=')[1].strip().strip("'\"")
                    print (language)
                    if language == 'ITA':
                        get_menu_ITA()
                    elif language == 'ENG':
                        get_menu_ENG()
                    else:
                        print("Lingua non supportata. Utilizzando inglese come predefinito.")
                        get_menu_ENG()
                    return
    else:
        print("File di configurazione 'config.py' non trovato. Utilizzando inglese come predefinito.")
        get_menu_ENG()

def start():
    config_file = 'config.py'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('LANGUAGE'):
                    language = line.split('=')[1].strip().strip("'\"")
                    if language == 'ITA':
                        start_ITA()
                    elif language == 'ENG':
                        start_ENG()
                    else:
                        print("Lingua non supportata. Utilizzando inglese come predefinito.")
                        start_ENG()
                    return
    else:
        print("File di configurazione 'config.py' non trovato. Utilizzando inglese come predefinito.")
        start_ENG()


def Select_language():
    while True:
        print("[1] English")
        print("[2] Italiano")
        choice = input("Enter the correct choice (Inserire la scelta corretta): ")

        if choice == '1':
            update_language_config('ENG')
            print("\nLanguage set to English.\n")
            break
        elif choice == '2':
            update_language_config('ITA')
            print("\nLingua impostata su Italiano.\n")
            break
        else:
            print("\nScelta non valida. Riprova.\n")

    get_menu()
    start()


def update_language_config(new_language):
    with open('config.py', 'w') as file:
        file.write(f"LANGUAGE = '{new_language}'\n")