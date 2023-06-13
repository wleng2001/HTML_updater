#!/usr/bin/python
import tkinter as tk
import analyze_copy as ac
import important_functions as important_functions

imf= important_functions.important_func()

window = tk.Tk()

app_name="html updater"
geo="540x360"

file_name=""
file=None
contents=""
path_file=None

if_search_subfolder=False
checkbox_name=["Podmień header", "Podmień artykuł", "Podmień stopkę"]
checkbox_html=["<header", "<article", "<footer"]
checkbox_variable=[]
for i in range(0, len(checkbox_name)):
    checkbox_variable.append(tk.BooleanVar())

def find_file():
    global file, contents, path_file, file_name
    file_name, file, contents=imf.open_file(ask=1, number=1, file_name=file_name, file=file, contents=contents, GUI=True)
    file_name=file_name.replace("/", imf.find_path_char(imf.find_os()))
    path_file.config(textvariable=tk.StringVar(window, file_name))
    
def draw_line(window, x, y, length):
    text="_"*length
    line=tk.Label(window, text=text)
    line.pack()
    line.place(x=x, y=y)

def graphic_mode(source_path):
    global file, contents, path_file, file_name
    window.title(app_name)
    window.geometry(geo)
    x, y=10, 10
    file_inf=tk.Label(window, text="Wybierz plik wzornika",fg="black")
    file_inf.pack()
    file_inf.place(x=x, y=y)
    #second row
    y=y+26
    find_file_b=tk.Button(window, text="...", width=2, command=lambda:find_file())
    find_file_b.pack()
    find_file_b.place(x=x, y=y)
    path_file=tk.Entry(window, textvariable=tk.StringVar(window, value="Lokalizacja pliku"), width=80)
    path_file.pack()
    path_file.place(x=x+24, y=y+4)
    #third row
    y=y+28
    choose_inf=tk.Label(window, text="Wybierz opcje")
    choose_inf.pack
    choose_inf.place(x=x, y=y)
    #rest row
    x_max_left=x
    y_add=26
    y=y+y_add
    x_add=150
    for i in checkbox_name:
        option_chb=tk.Checkbutton(window, text=i, variable=checkbox_variable[checkbox_name.index(i)], onvalue=1, offvalue=0)
        option_chb.pack()
        option_chb.place(x=x, y=y)
        
        if x==x_max_left:
            x=x+x_add
        else:   
            y=y+y_add
            x=x-x_add

    # second last row
    x=x_max_left
    y=y+20
    draw_line(window, x, y, 50)
    if_search_subfolder_chb=tk.Checkbutton(window, text="Przeszukuj podfoldery", variable=tk.BooleanVar(if_search_subfolder), onvalue=1, offvalue=0)
    if_search_subfolder_chb.pack()
    if_search_subfolder_chb.place(x=x, y=y+20)

    #last row

    def analyze_file():
        headers=[]
        for i in range(0,len(checkbox_variable)):
            if checkbox_variable[i].get()==True:
                headers.append(checkbox_html[i])
        ac.main_analyze_copy(headers, file_name, "", if_search_subfolder)
            
    x, y=430, 300
    allow_b=tk.Button(window, text="Podmień", width=10, command=lambda:analyze_file())
    allow_b.pack
    allow_b.place(x=x, y=y)
    window.mainloop()