import os

source = "text.txt"
destination = "C:\\........................"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileExistsError:
    print(source+" was not found")