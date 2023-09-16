# Status - OK
from requests import get
import ctypes
import os

def change_wallpaper():
  
  image = "background.bmp"
  getImage = get(f"https://raw.githubusercontent.com/Casanova5065/image/main/final.png").content
  wallpaper_path = os.path.expanduser("~\\Desktop\\") + image

  with open(wallpaper_path, "wb") as imageBytes:
    imageBytes.write(getImage)

  user32 = ctypes.windll.user32
  SPI_SETDESKWALLPAPER = 20

  r = user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 0x0001)
  if not r:
    print(ctypes.WinError())

if __name__=="__main__":
  pass



        
    