import os
import shutil
from_dir = "C:\\Users\\eaevi\\OneDrive\\Área de Trabalho\\Pastas\\Gamecode\\documentos"
to_dir = 'C:\\Users\\eaevi\\OneDrive\\Área de Trabalho\\Pastas\\Gamecode\\Donwloads'
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    from_dir, to_dir = os.path.splitext(file_name)
    print(from_dir)
    print(to_dir)
    if(from_dir == ""):
            continue
    if(from_dir in ['.txt','.doc','.docx','.pdf']):
        path1 = to_dir + "/" + file_name
        path2 = from_dir   + "/" + "documentos"
        path3 = from_dir   + "/" + "documentos" + "/" + file_name
        print(path1)
        print(path3)
        if(os.path.exists(path2)):
            print("Movendo" + file_name + ".....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo" + file_name + ".....")
            shutil.move(path1, path3) 