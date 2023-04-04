import os
import shutil
fromdir="C:/Users/Cliente Especial/Downloads/"
todir="C:/Users/Cliente Especial/Desktop/pro_102/Arquivos_Documentos/"
list_of_files = os.listdir(fromdir)
print(list_of_files)
for i in list_of_files:
    name,extension=os.path.splitext(i)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in [".txt",".doc",".docx",".pdf"]:
        path1=fromdir+'/'+name
        path2=todir
        path3=todir+'/'+"Arquivos_ Documentos"+'/'+name
        if os.path.exists(path2):
            print("movendo "+i+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("movendo "+i+"...")
            shutil.move(path1,path3)