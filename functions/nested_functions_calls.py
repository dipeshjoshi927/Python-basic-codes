# nested functions calls = functiom calls inside other function calls 
#                          innermost function calls are resolved first 
#                          returned value is used as argument for the next outer function 



#num = input("Enter a whole positive number:")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#this can be written as:
print(round(abs(float(input("Enter a whole positive number:")))))
