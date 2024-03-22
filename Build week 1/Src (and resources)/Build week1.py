import Language 
from colorama import Fore

def init():
    Language.Select_language()

def main():
    print(Fore.GREEN +
        " ____   __   __  _____   _____     ____    _____   ____    _____   _       ____  \n"
        "| __ )  \ \ / / |_   _| | ____|   |  _ \  | ____| | __ )  | ____| | |     / ___| \n"
        "|  _ \   \ V /    | |   |  _|     | |_) | |  _|   |  _ \  |  _|   | |     \___ \ \n"
        "| |_) |   | |     | |   | |___    |  _ <  | |___  | |_) | | |___  | |___   ___) |\n"
        "|____/    |_|     |_|   |_____|   |_| \_\ |_____| |____/  |_____| |_____| |____/ \n"
        + Fore.RESET)
    init()

if __name__ == "__main__":
    main()