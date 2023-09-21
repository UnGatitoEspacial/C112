import os
import shutil
#python puede reproducir archivos .exe,.msi, gif, .png, jpeg, .csv, .pdf, . xls, xlsx, .ppt, .ttx
from_dir = "C:\Users\Gato\Downloads"
to_dir="C:\Users\Gato\Downloads\MEmu Download"

list_of_files=os.listdir(from_dir)

#mueve todas las imagenes de la carpeta descargas a otra carpeta

for file_name in list_of_files:

    name, extension= os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpeg','.jpg','.jfif']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+"image_file"
        path3=to_dir+'/'+"image_file"+'/'+file_name
        
    #verifica si la carpeta /directorio ruta existe antes de muverla
    #de lo contrario, as una nueva carpeta /directorio luego muevela
    if os.path.exists(path2):
        print ("moviendo"+file_name+".....")
        #mueve de path 1 a path 3
        shutil.move(path1,path3)

    else:
        os.makedirs(path2)
        print ("moviendo"+ file_name+".....")
        shutil.move(path1.path3) 