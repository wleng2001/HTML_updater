#!/usr/bin/pythonpy
import tkinter as tk
from tkinter import messagebox as msg
import analyze_copy as ac
import important_functions as important_functions
from graphic_interface import *
import UPDATE_MODULE
import terminal
import os

imf= important_functions.important_func()

#info of version
date="2023-12-31"
name_app="HTML_updater"

GUI=True

file=None
file_name=""
contents=""

#update section-------------------------------------------------------------

UPDATE_MODULE.update_self(not GUI)

if GUI == True:
    window = tk.Tk()
    window.withdraw()

update_available=UPDATE_MODULE.update_check(date, name_app)
if update_available==None:
    if GUI == False:
        print("You don't have internet connection.")
    else:
        msg.showinfo(title=name_app, message="You don't have internet connection.")
elif update_available==True:
    if GUI == False:
        print("Update is available!")
        ask=input("Do you want download it now (Y/n): ")
        ask=ask.upper()
        if ask=="Y":
            if_download=UPDATE_MODULE.download_update_repo("https://codeload.github.com/wleng2001/HTML_updater/zip/refs/heads/main", os.getcwd())
            if if_download==False:
                print("Lost connection file wasn't downloaded")
    else:
        ask = msg.askquestion(title=name_app, message="Update is available!\nDownload it now?")
        if ask == "yes":
            if_download=UPDATE_MODULE.download_update_repo("https://codeload.github.com/wleng2001/HTML_updater/zip/refs/heads/main", os.getcwd())
            if if_download==False:
                msg.showinfo("Lost connection file wasn't download")

else:
    print("App is current")

#work section---------------------------------------------------------------

if GUI==True:
    graphic_mode(file_name)



