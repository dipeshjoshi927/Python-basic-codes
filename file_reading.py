try:
    with open('C:\\Users\\dipes\\OneDrive\\Desktop\\test.txt') as file:
         print(file.read())
except FileNotFoundError:
     print("File not found")


