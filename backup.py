import os
import shutil

source = input("Enter the source folder/file: ")
dest = input("Enter the destination folder/file: ")

source = source+"/"
dest = dest+"/"

list_of_files = os.listdir(source)

for file in list_of_files:
   shutil.copy((source+file) , dest)

