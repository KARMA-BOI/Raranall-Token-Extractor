import os
import tempfile
import shutil
import re
import subprocess
import time
import ctypes

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREY = '\033[90m'
RESET = '\033[0m'

def generate_banner():

    banner = RED + """
██████╗  █████╗ ██████╗  █████╗ ███╗   ██╗ █████╗ ██╗     ██╗     
██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██║     ██║     
██████╔╝███████║██████╔╝███████║██╔██╗ ██║███████║██║     ██║     
██╔══██╗██╔══██║██╔══██╗██╔══██║██║╚██╗██║██╔══██║██║     ██║     
██║  ██║██║  ██║██║  ██║██║  ██║██║ ╚████║██║  ██║███████╗███████╗    GITHUB.COM/KARMA-BOI
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝    CREATED BY KARMA
""" + RESET

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
    os.system('cls')
    generate_banner()
    input(GREY + "[>] PRESS ENTER TO START THE PROGRAM" + RESET)
    os.system('cls')
    generate_banner()
    while True: 
        archive_folder = input(GREY + "[>] RAR FILES DIRECTORY: " + RESET)
        if os.path.isdir(archive_folder):
            print(GREY + "[>] VALID DIRECTORY" + RESET)
            time.sleep(2)
            os.system('cls')
            generate_banner()
            break
        else:
            print(GREY + "[>] INVALID DIRECTORY..." + RESET)
            time.sleep(2)
            os.system('cls')
            generate_banner()
    os.system('cls')
    generate_banner()
    password = input(GREY + "[>] RAR FILES PASSWORD: " + RESET)
    print(GREY + "[>] VALID PASSWORD" + RESET)
    time.sleep(2)
    os.system('cls')
    generate_banner()
    

    output_file_path = os.path.join(os.getcwd(), 'extracted_tokens.txt')
    extracted_tokens = set()
    tokens = []
    total_tokens_extracted = 0


    print(GREY + "[>] STARTING EXTRACTION PROCESS" + RESET)
    time.sleep(2)
    os.system('cls')
    generate_banner()
    with open(output_file_path, 'w') as output_file:
        for filename in os.listdir(archive_folder):
            archive_path = os.path.join(archive_folder, filename)
            if os.path.isfile(archive_path) and (archive_path.endswith('.rar')):
                try:
                    print(GREY + "[+] EXTRACTING FROM: " + RESET + f"{archive_path}")
                    total_tokens_extracted += len(tokens)
                    tokens = extract_tokens_from_rar(archive_path, password, extracted_tokens)
                    for token in tokens:
                        output_file.write(token + '\n')
                except Exception as e:
                    print(GREY + "[+] ERROR EXTRACTING FROM " + RESET + f"{archive_path}" + {e})
    time.sleep(2)
    os.system('cls')
    generate_banner()
    print(GREY + f"[>] SUCCESSFULLY EXTRACTED {total_tokens_extracted} TOKENS" + RESET)
    time.sleep(2)
    os.system('cls')
    generate_banner()
    print(GREY + f"[>] TOKENS EXTRACTED TO: {output_file_path}" + RESET)
    time.sleep(2)
    os.system('cls')
    generate_banner()
    input(GREY + "[>] PRESS ENTER TO CLOSE THE PROGRAM" + RESET)

if __name__ == "__main__":
    main()
