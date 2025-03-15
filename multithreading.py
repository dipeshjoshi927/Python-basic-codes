# thread = a flow of execution. Like a separate order of instructions.
#              However each thread takes a turn running to achieve concurrency 
#              GIL (Global Interpreter Lock), allows oly one thread to hold the control of python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing
# io bound = program/task spends most of it's time waiting for external events (user input,web scraping)
#             use multithreading


import threading
import time

def eat():
    time.sleep(2)
    print("You ate breakfast")

def drink():
    time.sleep(3)
    print("You drank water")

def coding():
    time.sleep(4)
    print("You are coding")

x = threading.Thread(target=eat, args=())        #Multithreading 
x.start()

y = threading.Thread(target=drink, args=())
y.start()

z = threading.Thread(target=coding, args=())
z.start()

x.join()
y.join()
z.join()


#eat()
#drink() 
#coding()



print(threading.active_count())      # prints number of active threads 
print(threading.enumerate())         # prints the active threads 
print(time.perf_counter())
