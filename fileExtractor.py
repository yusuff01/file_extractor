import os
import shutil
import time
import math

# given a USB drive to sort through
##drive = input("Enter input drive directory: ")
##drive = "C:\\Users\\yusuf\\Pictures\\flir pics"
drive = "D:\\greylaptopBackup\\cetin\\Pictures"

# enter directory to store outputted sorted files
##output = input("Enter output directory for sorted files: ")
output = "Z:\\output" #cwd

# valid filetypes to include in the extracting
filetype = (".jpg", ".jpeg", ".png", ".avi", ".mp4", ".mov")


# recurse through each subfolder 
print(os.listdir(drive))
i = 0

def getFile(directory):

##    print("DIR: " + directory)

    if len(next(os.walk(directory))[1]) == 0: ## if no further folders exist in dir
        
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f): ## makes sure that f is not a folder

                if f.lower().endswith(filetype): ## ensures the right filetype
                    
                    print("File number: " + f)
                    shutil.copy2(f, output)
            

    else: ## there's at least one folder in the dir

        for filename in os.listdir(directory): ## checks for files
            f = os.path.join(directory, filename)
            if os.path.isfile(f): ## makes sure that f is not a folder

                if f.lower().endswith(filetype): ## ensures the right filetype

                    print("File number: " + f)
                    shutil.copy2(f, output)
        
        for folder in os.listdir(directory):

            f = os.path.join(directory, folder)
            if os.path.isdir(f): ## makes sure that f is a folder, not file
            
##                print(folder)
            
                getFile( os.path.join(directory,folder) )
                
tStart = time.time()
getFile(drive)
print("Extracting files took: " + str(math.floor(time.time() - tStart)) + " seconds.")

