# map() = applies a function to each item in an iterable (list,tuple,etc)
# map(function,iterable)

store = [("Shirt",20.00),
        ("Pants",25.00),
        ("Jacket",50.00),
        ("Gloves",10.00)]

to_nrs = lambda data:(data[0],data[1]*133.47)
store_nrs = list(map(to_nrs,store))

for i in store_nrs:
    print(i)

