import numpy as np

arr = np.array([[1,4,3,2,5,6],[4,5,6,7,8,9]]) #for 2-D array the number of items inside the array should be same
# use ([],ndmin= ) to create a n-dimension array
print(arr.ndim) # to check how many dimension that array has

#print(arr[1,5]) # access 2D array
# can use negative indexing to access last element(-1)

# for array slicing can use indexing [start:end] or [start:end:step]
#print(arr[1, 1:5])

# can use arr.dtype to check the type of data
# can define data type while creating array ([], dtype='i,u,f,S,U4') 4 iss used to define the size

# astype() can be used to convert exsisting datatype to another

#asarray() is used to change the list into array

array =np.array([1.1, 2.2, 3.3, 4.4, 5.5])

newarray = array.astype('int')
#print(newarray)

# to copy data into new array 
x1 = array.copy()
#print(x1)

array1 = np.array([[1,2,3,4,5],[2,3,4,5,6]])
x = array1.copy()
y = array1.view()
print(x)
print(y.base) # base helps to check if the array owns the data

# to check the shape of an array
# to check the size (arraay.size) can be used

print(x.shape)



#iterate array using nditer

for c in np.nditer(array):
    print(c)
    
# join array
a = np.array([[1,2,3],[5,6,7]])
b = np.array([[4,5,6],[7,8,9]])
joinedArr = np.concatenate((a, b),axis=1) 
# can also use stack() ,hstack(), vstack(), dstack()
#joinedArr = np.stack((a, b), axis=1)

print(joinedArr)

# np.array_split(array_name, numberOfArray)

#Search array
search = np.where(arr == 5)
print (search)

sorted = np.searchsorted(array, 3.3)
print(sorted)

# sort() is used to sort array
print(np.sort(arr))

#random data
rand = np.random.randint(10,100,(4,3)) #(from,to,(row,column))

#evenly spaced values

evenly = np.linspace(1,3,3) #(start,end, how many values)

aranged = np.arange(1,10,2) #(start,end, step)

#Mathematical operations on a np array
summed = np.add(a,b)
subtracted = np.subtract(a,b)
divided = np.divide(a,b)
multiplied = np.multiply(a,b)

#Array manipulation

trans = np.transpose(a) #Transpose

#to reshape an array from 1-D to 2-D
z = array1.reshape(5,2) # (5,2,-1 can also be used )
print(z)
# for 3-D we can use arr.reshape(2,3,2) => 2 arrays that contain 3 arrays with 2 element
