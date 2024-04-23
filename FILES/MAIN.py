import os
import colorama
from colorama import Fore, Style
import tempfile
import shutil
import re
import subprocess
import time
import ctypes

def generate_banner():
    colorama.init()  # Initialize colorama for Windows

    banner = f"""
{Fore.RED}
██████╗  █████╗ ██████╗  █████╗ ███╗   ██╗ █████╗ ██╗     ██╗     
██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██║     ██║     
██████╔╝███████║██████╔╝███████║██╔██╗ ██║███████║██║     ██║     
██╔══██╗██╔══██║██╔══██╗██╔══██║██║╚██╗██║██╔══██║██║     ██║     
██║  ██║██║  ██║██║  ██║██║  ██║██║ ╚████║██║  ██║███████╗███████╗    GITHUB.COM/KARMA-BOI
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝    CREATED BY KARMA
"""

    print(banner)

def extract_tokens_from_rar(archive_path, password, extracted_tokens):
    temp_dir = tempfile.mkdtemp()
    try:
        subprocess.run([r'UnRAR.exe', 'x', '-p' + password, archive_path], cwd=temp_dir, stdout=0, stderr=subprocess.PIPE)
        tokens_list = []
        for root, devs, files in os.walk(temp_dir):
            for file in files:
                if file.endswith('.txt'):
                    txt_file_path = os.path.join(root, file)
                    tokens_list.extend(extract_tokens_from_txt(txt_file_path, extracted_tokens))
        return tokens_list
    finally:
        shutil.rmtree(temp_dir)


def extract_tokens_from_txt(file_path, extracted_tokens):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        # Use regex to find Discord tokens
        tokens = re.findall(r"Token:\s+([A-Za-z0-9._-]+)", content)
        unique_tokens = [token for token in tokens if token not in extracted_tokens]
        extracted_tokens.update(unique_tokens)
        return unique_tokens

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("CREATED BY KARMA-BOI | RARANALL")
    generate_banner()
    while True: 
        archive_folder = input("[>] RAR FILES DIRECTORY: ")
        if os.path.isdir(archive_folder):
            print("[>] VALID DIRECTORY")
            time.sleep(2)
            os.system('cls')
            generate_banner()
            break
        else:
            print("[>] INVALID DIRECTORY...")
            time.sleep(2)
            os.system('cls')
            generate_banner()
    os.system('cls')
    generate_banner()
    password = input("[>] RAR FILES PASSWORD: ")
    print("[>] VALID PASSWORD")
    time.sleep(2)
    os.system('cls')
    generate_banner()
    

    output_file_path = os.path.join(os.getcwd(), 'extracted_tokens.txt')
    extracted_tokens = set()
    tokens = []
    total_tokens_extracted = 0


    print("[>] STARTING EXTRACTION PROCESS...")
    time.sleep(2)
    os.system('cls')
    generate_banner()
    with open(output_file_path, 'w') as output_file:
        for filename in os.listdir(archive_folder):
            archive_path = os.path.join(archive_folder, filename)
            if os.path.isfile(archive_path) and (archive_path.endswith('.rar')):
                try:
                    print(f"[+] EXTRACTING FROM {archive_path}...")
                    total_tokens_extracted += len(tokens)
                    tokens = extract_tokens_from_rar(archive_path, password, extracted_tokens)
                    for token in tokens:
                        output_file.write(token + '\n')
                except Exception as e:
                    print(f"[-] ERROR EXTRACTING FROM {archive_path}: {e}")
    time.sleep(2)
    os.system('cls')
    generate_banner()
    print(f"[>] SUCCESSFULLY EXTRACTED {total_tokens_extracted} TOKENS")
    time.sleep(2)
    os.system('cls')
    generate_banner()
    print(f"TOKENS EXTRACTED TO: {output_file_path}")
    time.sleep(2)
    os.system('cls')
    generate_banner()
    input("[>] PRESS ENTER TO CLOSE THE PROGRAM")

if __name__ == "__main__":
    main()
