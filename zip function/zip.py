# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each elements

usernames = ["Raju","Shyam","Baburao"]
passwords = ["Raju@123","Shyam@123","Baburao@123"]
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = zip(usernames,passwords,login_date)
for i in users:
    print(i)