# Hellcat Ransomware 🇬🇧

This project is a mini ransomware demonstration to understand the operation of this type of malware. It was created as part of a school project to present during an Open Day.

The main features of the script include:

1. **RSA Key Pair Generation**: The script generates an RSA key pair (public key and private key) to encrypt and decrypt files.

2. **File Encryption**: The script encrypts all files in the "exemple_dir" directory (at the root of the project) using the previously generated public key.

3. **File Decryption**: The script decrypts all files in the "exemple_dir" directory (at the root of the project) using the previously generated private key.

4. **Display of a tkinter Window**: The script displays a tkinter window with a ransom message.

**Disclaimer**: This project was created for educational purposes and should not be used for malicious intent. The authors will not be held responsible for any damage caused by users of this script.

[Versions française ici](README.md) 🇫🇷 

## Installation

You can install the project by cloning the repository using the following command:

```
git clone https://github.com/Hellcat-IV/Ransomware.git
```
Don't forget to install the dependencies:   
```
pip install -r requirements.txt
```

## Usage

To use the script, run the following command:
    
```
python3 ransom.py -h
```

## Contributors

- [@Kenoor](https://github.com/bxsic-fr)
- [@Valmar](https://www.github.com/CalValmar)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for more details.

GNU General Public License v3.0 © [HellCat-IV](https://github.com/Hellcat-IV)