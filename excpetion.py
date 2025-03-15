# exception = events detected during execution that interrupt the flow of a program


try:
     numerator = int(input("Enter a number to divide: "))
     denominator = int(input("Ener a number to divide by: "))
     result = numerator / denominator
    
except ZeroDivisionError as e:
     print(e)
     #print("you can't divide by zero idiot")
except ValueError:
     print("Use only numbers idiot")
#except Exception:
 #    print("Something went wrong")
     
else:
     print(result)


    






















