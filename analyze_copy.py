import important_functions as important_functions
imf= important_functions.important_func()
import os

headers_content=[]


def modify_headers(headers):
    new_headers=[]
    for i in headers:
        if i[-1]==">":
            new_headers.append(i[:-1])
        else:
            new_headers.append(i)
    return new_headers

def end_headers_generator(headers):
    end_headers=[]
    for i in headers:
        end_headers.append(i[0]+"/"+i[1:]+">")
    return end_headers
        
def analyze_source(headers, file_name, file, contents):
    headers=modify_headers(headers)
    end_headers=end_headers_generator(headers)
    headers_i=0
    for i in headers:
        copy_text=""
        analyze_header="<"
        end_header=""
        check_end_header=False
        if_analyze_header=False
        if_copy_text=False
        for j in contents:
            if j=="<" and if_analyze_header==False:
                if_analyze_header=True
                continue
            if if_analyze_header==True and if_copy_text==False:
                if j==" " or j==">":
                    if i==analyze_header:
                        if_copy_text=True
                        copy_text+=analyze_header+j
                        continue
                    else:
                        if_analyze_header=False
                        analyze_header="<"
                        continue
                analyze_header+=j
            if if_copy_text==True:
                copy_text+=j
                if j=="<":
                    end_header+=j
                    check_end_header=True
                    continue
                if check_end_header==True:
                    end_header+=j
                    if j==">" and end_headers[headers_i]==end_header:
                        headers_content.append(copy_text)
                        headers_i=headers_i+1
                        break
                    elif j==">" and end_header[headers_i]!=end_header: 
                        end_header=""
                        check_end_header=False

def find_files_to_edit(file_name, search_subfolders):
    def search_files(files_to_edit_temp, loc):
        folders=[]
        for i in files_to_edit_temp:
            if os.path.isfile(loc+i)==False:
                if search_subfolders==True:
                    folders.append(loc+i)
            else:
                files_to_edit.append(loc+i)
        return folders  
    
    def look_subfolders(loc, folders):
        if search_subfolders==True:
            print("przeszukuję foldery")
            for i in folders:
                print(f"Jestem w folderze: {i}")
                files=os.listdir(loc+i)
                foldersi=search_files(files, loc+i)
                print(f"foldersi: {foldersi}")
                print(foldersi)
                if foldersi!=['']:
                    look_subfolders(loc+i, foldersi)
                
    files_to_edit=[]
    
    loc=""
    path_char=imf.find_path_char(imf.find_os())
    loc_temp=file_name.split(path_char)[:-1]
    if(loc_temp==[]):
        loc=file_name
    else:
        for i in loc_temp:
            loc+=i+path_char
    os.chdir(loc)
    files_to_edit_temp=os.listdir()
    print(f"tymczasowe: {files_to_edit_temp}")
    folders=search_files(files_to_edit_temp, loc)
    print(f"foldery: {folders}")
    look_subfolders(loc, folders)
    print(files_to_edit)
    return files_to_edit

def edit_found_files(files_to_edit, headers):
    def open_file(file_name):
        file=open(file_name, 'r', errors='ignore', encoding='utf-8')
        content=file.read()
        file.close()
        return content
    
    end_headers=end_headers_generator(headers)
    
    for i in files_to_edit:
        print(f"Otwieram plik: {i}")
        file_content=open_file(i)
        headers_i=0
        for j in headers:
            copy_text=""
            analyze_header="<"
            end_header=""
            check_end_header=False
            if_analyze_header=False
            if_change_text=False
            file_content_temp=file_content
            for k in file_content:
                file_content_temp=file_content_temp[1:]
                if k=="<" and if_analyze_header==False:
                    if_analyze_header=True
                    copy_text=copy_text+k
                    continue
                if if_analyze_header==True and if_change_text==False:
                    if k==" " or k==">":
                        print(f"analizowany nagłówek: {analyze_header}")
                        if j==analyze_header:
                            print("zgodny")
                            if_change_text=True
                            copy_text=copy_text[0:-len(analyze_header)]+headers_content[headers_i]
                            continue
                        else:
                            if_analyze_header=False
                            analyze_header="<"
                            copy_text=copy_text+k
                            continue
                    analyze_header+=k
                if if_change_text==True:
                    if k=="<":
                        end_header+=k
                        check_end_header=True
                        continue
                    if check_end_header==True:
                        end_header+=k
                        if k==">" and end_headers[headers_i]==end_header:
                            copy_text=copy_text+file_content_temp
                            headers_i=headers_i+1
                            print(f"zamykam nagłówek: {end_header}")
                            break
                        elif k==">" and end_header[headers_i]!=end_header: 
                            end_header=""
                            check_end_header=False
                if if_change_text==False:
                    copy_text=copy_text+k
            file=open(i, 'w', encoding='utf-8', errors='ignore')
            file.write(copy_text)
            file.close()
            file_content=copy_text
        

def main_analyze_copy(headers, file_name, file,  search_subfolder, only_html=True):
    #headers is table
    print(headers)
    file=open(file_name, "r", encoding='utf-8', errors='ignore')
    contents=file.read()
    analyze_source(headers, file_name, file, contents)
    file.close()
    files_to_edit=find_files_to_edit(file_name, search_subfolder)
    edit_found_files(files_to_edit, headers)
    return files_to_edit

