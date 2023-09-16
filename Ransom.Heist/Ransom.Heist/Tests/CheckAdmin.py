import ctypes

def IsAdmin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False
	
print(IsAdmin())
	
