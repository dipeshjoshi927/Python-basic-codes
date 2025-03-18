text = "Have a nice day!"

with open('text.txt','a') as file: # r =read| w = write | a = add
    file.write(text)
