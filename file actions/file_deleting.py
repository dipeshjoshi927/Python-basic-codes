import os
import shutil
path = 'folder'
try:
    #os.remove(path)             # delete a file  
    os.removedirs(path)         #delete an empty directory
    #shutil.rmtree(path)      #delete a diretory containing files
except FileNotFoundError:
    print("File cannot be found")
except PermissionError:
    print("You do not have permission")
except OSError:
    print("you cannot delete that using that function")    

else: 
    print(path+" was deleted")