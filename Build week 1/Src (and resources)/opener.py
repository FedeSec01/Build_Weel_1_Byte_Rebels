import os
import subprocess

def open_png_image():
    image_path="/home/kali/Documents/Programmazione_Epicode/Python/BW1/Screenshot_2024-03-20_095916(1).png"
    if not os.path.exists(image_path):
        print(f"Errore: il file '{image_path}' non esiste.")
        return

    try:
        subprocess.Popen(['xdg-open', image_path])  # Apri l'immagine PNG utilizzando il programma predefinito del sistema
    except Exception as e:
        print(f"Errore nell'apertura dell'immagine: {e}")


def open_pdf_based_on_language():
    # Verifica se il file di configurazione esiste
    config_file = 'config.py'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('LANGUAGE'):
                    LANGUAGE = line.split('=')[1].strip().strip("'\"")
                    break
            else:
                print("Lingua non specificata nel file di configurazione.")
                return
    else:
        print("File di configurazione 'config.py' non trovato.")
        return

    # Definisce il percorso del file PDF in base alla lingua
    if LANGUAGE == 'ITA':
        pdf_path = '/home/kali/Documents/Programmazione_Epicode/Python/BW1/Byte_Rebels_-_Build_Week_ITA.pdf'
    elif LANGUAGE == 'ENG':
        pdf_path = '/home/kali/Documents/Programmazione_Epicode/Python/BW1/Byte_Rebels_-_Build_Week_ENG.pdf'
    else:
        print("Lingua non supportata nel file di configurazione.")
        return

    # Apri il PDF utilizzando il programma predefinito del sistema
    try:
        subprocess.Popen(['xdg-open', pdf_path])  # Apri il PDF su sistemi Linux
    except Exception as e:
        print(f"Errore nell'apertura del PDF: {e}")

def open_preventivo_based_on_language():
    # Verifica se il file di configurazione esiste
    config_file = 'config.py'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('LANGUAGE'):
                    LANGUAGE = line.split('=')[1].strip().strip("'\"")
                    break
            else:
                print("Lingua non specificata nel file di configurazione.")
                return
    else:
        print("File di configurazione 'config.py' non trovato.")
        return

    # Definisce il percorso del file del preventivo in base alla lingua
    if LANGUAGE == 'ITA':
        preventivo_path = '/home/kali/Documents/Programmazione_Epicode/Python/BW1/Theta_S.R.L_ITA.pdf'
    elif LANGUAGE == 'ENG':
        preventivo_path = '/home/kali/Documents/Programmazione_Epicode/Python/BW1/Theta_S.R.L_ENG.pdf'
    else:
        print("Lingua non supportata nel file di configurazione.")
        return

    # Apri il preventivo utilizzando il programma predefinito del sistema
    try:
        subprocess.Popen(['xdg-open', preventivo_path])  # Apri il preventivo su sistemi Linux
    except Exception as e:
        print(f"Errore nell'apertura del preventivo: {e}")

def open_report_phpmyadmin_based_on_language():
    # Verifica se il file di configurazione esiste
    config_file = 'config.py'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('LANGUAGE'):
                    LANGUAGE = line.split('=')[1].strip().strip("'\"")
                    break
            else:
                print("Lingua non specificata nel file di configurazione.")
                return
    else:
        print("File di configurazione 'config.py' non trovato.")
        return

    # Definisce il percorso del file del report in base alla lingua
    if LANGUAGE == 'ITA':
        report_phpmyadmin_path = '/home/kali/Documents/Programmazione_Epicode/Python/BW1/report_phpmyadmin_ITA.pdf'
    elif LANGUAGE == 'ENG':
        report_phpmyadmin_path = '/home/kali/Documents/Programmazione_Epicode/Python/BW1/report_phpmyadmin_ENG.pdf'
    else:
        print("Lingua non supportata nel file di configurazione.")
        return
    
    # Apri il report utilizzando il programma predefinito del sistema
    try:
        subprocess.Popen(['xdg-open', report_phpmyadmin_path])  # Apri il prevreportentivo su sistemi Linux
    except Exception as e:
        print(f"Errore nell'apertura del report: {e}")

def open_report_dvwa_based_on_language():
    # Verifica se il file di configurazione esiste
    config_file = 'config.py'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('LANGUAGE'):
                    LANGUAGE = line.split('=')[1].strip().strip("'\"")
                    break
            else:
                print("Lingua non specificata nel file di configurazione.")
                return
    else:
        print("File di configurazione 'config.py' non trovato.")
        return

     # Definisce il percorso del file del report in base alla lingua
    if LANGUAGE == 'ITA':
        report_dvwa_path = '/home/kali/Documents/Programmazione_Epicode/Python/BW1/Report_DVWA_ITA.pdf'
    elif LANGUAGE == 'ENG':
        report_dvwa_path = '/home/kali/Documents/Programmazione_Epicode/Python/BW1/Repor_DVWA_ENG.pdf'
    else:
        print("Lingua non supportata nel file di configurazione.")
        return
    
    # Apri il report utilizzando il programma predefinito del sistema
    try:
        subprocess.Popen(['xdg-open', report_dvwa_path])  # Apri il prevreportentivo su sistemi Linux
    except Exception as e:
        print(f"Errore nell'apertura del report: {e}")