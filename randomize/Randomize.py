import random
x = random.randint(1,6)
y = random.random()

myList = ['Rock','Paper','Scissors']
z = random.choice(myList)

cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
random.shuffle(cards)
print(z)