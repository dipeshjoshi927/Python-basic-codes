# sort() method = used with lists
# sort() function = used with iterables

'''students = ["Ram","Shyam","Hari","Condo","Ishao"]

students.sort()
students.sort(reverse=True)

for i in students:
    print(i)'''


'''students = ("Ram","Shyam","Hari","Condo","Ishao")
#sorted_students = sorted(students)
sorted_students = sorted(students,reverse=True)
for i in sorted_students:
    print(i)'''

'''students = [("Squidward","F", 60)
            ,("Spongebob","D", 55)
            ,("Patrick","A", 40)
            ,("Sandy","B", 85)
            ,("Mr. Krabs","C", 45)
            ]

grade = lambda grades:grades[1]
age = lambda age:age[2]
#students.sort(key=grade)
#for reverse
students.sort(key=age,reverse=True)

for i in students:
    print(i)'''

students = (("Squidward","F", 60)
            ,("Spongebob","D", 55)
            ,("Patrick","A", 40)
            ,("Sandy","B", 85)
            ,("Mr. Krabs","C", 45))

grade = lambda grades:grades[1]
age = lambda age:age[2]
sorted_students =sorted(students,key=age,reverse=True)

for i in sorted_students:
    print(i)
