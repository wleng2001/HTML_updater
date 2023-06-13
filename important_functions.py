import sys
import os
import requests
from tkinter import filedialog

class important_func:
    def __init__(self):
        self.sys=self.find_os() 
        self.path_char=self.find_path_char(self.sys)
        
    def find_os(self):
        #return type of operating system
        if sys.platform=='win32':
            return 'win'
        elif sys.platform=='linux' or sys.platform=='linux2':
            return 'linux'
        else:
            return 'OS X'
        
    def find_path_char(self, sys):
        if sys=='win':
            return '\\'
        elif sys=='linux':
            return '/'
        
    def cls(self):
        #clear terminal
        if self.sys=="win":
            os.system("cls")
        elif self.sys=="linux":
            os.system("clear")
            
    def internet_connection(self, timeout):
        #check internet connection if you don't have it it return False else return True
        #timeout it's time of waiting to respond
        try:
            requests.head("https://google.com/", timeout=timeout)
            return True
        except requests.ConnectionError:
            return False
        
    def open_file(self, ask, number, file_name, file, contents, GUI):
        if ask==number:
            if GUI==True:
                file_name=filedialog.askopenfilename(initialdir=os.getcwd())
                print("Wybierz plik: "+file_name)
            else:
                file_name=input("Wpisz ścieżkę do pliku: ")
            try:
                file=open(file_name, 'r')
                contents=file.read()
                return file_name, file, contents
            except:
                return file_name, file, contents
        return file_name, file, contents
            
      
#test=important_func()
#print(test.sys)