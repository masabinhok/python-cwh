#os is a built in module, importing os in our file.
import os 

#specify the path of the directory you wanna list
path="./"

#list all files in the specified path: os.listdir
l_files = os.listdir(path)

#print each file and directory name 
for item in l_files:
    print(item)