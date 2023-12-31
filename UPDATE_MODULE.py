#You can read mor on github website: https://github.com/wleng2001/UPM-UPdate_Module_for_app
#check and install update
#import-------------------------
from datetime import datetime
from github import Github
#from git import Repo
import git
from os import getcwd, listdir, rename, rmdir, remove
from shutil import rmtree
from sys import platform, executable, argv
import ctypes
import requests
from  zipfile import ZipFile
import tkinter as tk
from tkinter import messagebox as msg
#variables----------------------
last_update="2023-12-31"
repo_name="UPM-UPdate_Module_for_app"
url="https://raw.rawgit.net/wleng2001/UPM-UPdate_Module_for_app/main/UPDATE_MODULE.py"
new_version_name="UPDATE_MODULE.py"
#turn on admin permission
def admin():#put it in second line after import UPDATE_MODULE
    if find_os()=='win':
        if ctypes.windll.shell32.IsUserAnAdmin()==False:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv), None, 1)
            quit()

#update check-------------------
def update_check(last_update, repo_name):
    last_date=datetime.fromisoformat(last_update)
    g=Github()
    try:
        for i in g.search_repositories(repo_name):
            repo=i
        date=repo.pushed_at
        if date.date()==last_date.date():
            return False
        else:
            return True
    except:
        return None

#find os
def find_os():
    if platform=='win32':
        return 'win'
    elif platform=='linux' or platform=='linux2':
        return 'linux'
    else:
        return 'OS X'

def find_os_f_s():
    if platform=='win32':
        return '\\'
    elif platform=='linux' or platform=='linux2':
        return '/'
    else:
        return '/'

#remove files and destination

def remove_d_f(destination):
    file_sep=find_os_f_s()
    git_in_d=False
    for i in destination.split(file_sep):
        if '.git' ==i:
            git_in_d=True
            break
    if git_in_d==False:
        try:
            remove(destination)
        except:
            for i in listdir(destination):
                file=destination+file_sep+i
                try:
                    remove(file)
                except:
                    try:
                        rmdir(file)
                    except:
                        remove_d_f(file)
            rmtree(destination, ignore_errors=True)


#move download files
def move_files(file_path, destination, files=[]): #You don't have to give, which file you want to move if you want move all files in path
    file_sep=find_os_f_s()
    if files!=[]:
        for i in files:
            try:
                remove_d_f(destination+file_sep+i)
                rename(file_path+file_sep+i, destination)
            except:
                print(f"Error! File {i} doesn't exist")
    else:
        for i in listdir(file_path):
            if i!=".git":
                if i in listdir(getcwd()):
                    remove_d_f(destination+file_sep+i)
                rename(file_path+file_sep+i, destination+file_sep+i)

#download update
def download_update_repo(url,path):#if you don't want to move all files you can add to files in your repo file "files_to_move.txt", which will be include files to move separate by ", "
    file_sep=find_os_f_s()
    next=False
    if "codeload." in url:
        folder=url.split('/')[-5]
        r=requests.get(url, allow_redirects=True)
        open(path+file_sep+folder+'.zip', 'wb').write(r.content)
        with ZipFile(path+file_sep+folder+'.zip', 'r') as zip_object:
            zip_object.extractall(path, members=None, pwd=None)
        next=True
        folder+='-main'
    else:
        try:
            folder=url.split('/')[-1]
            git.Git(path).clone(url)
            next=True
        except:        
            return False
    if next==True:
        try:
            files=open(path+file_sep+folder+file_sep+"files_to_move.txt",'r').read().split(', ')
        except:
            files=[]
        move_files(path+file_sep+folder, path, files)
        remove_d_f(path+file_sep+folder)
        remove_d_f(path+file_sep+folder[:-5]+'.zip')
        print(f'Please remove manually "{path+file_sep+folder}" folder')
        return True

def download_update_file(url, path, file_name): #url must be in raw format for example from rawgit.net website
    try:
        file=requests.get(url)
        file=file.content
        open(file_name,'wb').write(file)
        return True
    except:
        return False


def question_window(question, window_name):
    window = tk.Tk()
    window.withdraw()
    return msg.askquestion(window_name, question)
    

#full update of update module
def update_self(terminal_mode = True):
    if terminal_mode == False:
        window = tk.Tk()
        window.withdraw()
    update_available=update_check(last_update, repo_name)
    if update_available==None:
        if terminal_mode == True:
            print("You don't have internet connection.")
        else:
            msg.showinfo(title = "UPM", message = "You don't have internet connection.")
    elif update_available==True:
        if terminal_mode == True:
            print("Update of updater is available!")
            ask=input("Do you want download it now (Y/n): ")
            ask=ask.upper()
            if_download=None
            if ask=="Y":
                if_download=download_update_file(url,getcwd(), new_version_name)
            if if_download==False:
                print("Lost connection, file wasn't downloaded")
            else:
                print("Updater was updated.")
        else:
            ask = question_window("Update is available!\nDownload it now?", "UPM")
            if_download = None
            if(ask == "yes"):
                if_download = download_update_file(url, getcwd(), new_version_name)
            if if_download == False:
                msg.showinfo("UPM", "Lost connection, file wasn't download")
            else:
                msg.showinfo("UPM","Updater was updated")
    else:
        if terminal_mode == True:
            print("Updater is current")
        else:
            msg.showinfo("UPM", "Updater is current")
