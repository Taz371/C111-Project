# Used to access Operating System
import os
# Used to copy files and move them
import shutil

source = "C:/Users/tazim/OneDrive/Desktop/Cool Python Projects/Moving Files/Downloads"
destination = "C:/Users/tazim/OneDrive/Desktop/Cool Python Projects/Moving Files/New_Downloads"


list_of_files = os.listdir(source)
#print(list_of_files)

for i in list_of_files:
    print(os.path.splitext(i))
    
