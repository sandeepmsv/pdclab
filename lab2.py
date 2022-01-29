''' Q. Write a program to perform two function: 
a. Sum of square
b. Sleep function


- Perform it using sequential approach
- Perform it using multithread approach
- Calculate and Print the time taken by both to execute. '''


from threading import *
import time
class MyThread():
    def __init__(self,sleeptime):
        self.sleeptime = sleeptime
   
    def squares_func(self,number):
        sum1 = 0
        for j in range(1,number):
            sum1 += j*j
        print(f"sum of square:{sum1}")

    def sequential_exec(self,echo):
        begin_time = time.time()
        self.squares_func(echo)
        time.sleep(self.sleeptime)
        end_time = time.time()
        return end_time - begin_time



number = int(input("Enter Number to be squared:"))
sleeptime = int(input("Enter sleeptime:"))
obj = MyThread(sleeptime)
begin_time = time.time()
t1 = Thread(target=obj.squares_func, args = (number,))
t2 = Thread(target = time.sleep,args = (sleeptime,))
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print(f"multi_threaded_time: {end_time - begin_time}")
print(f"sequential time execution:{obj.sequential_exec(number)}")


    
    
    



