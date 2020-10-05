#bindal
#python code for dice roll using random python function
import random
min = 1
max = (5+1)

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dice again?")
    
    
    
#python code for tower of hanoi
def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    if n == 1: 
        print "Move disk 1 from rod",from_rod,"to rod",to_rod 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print "Move disk",n,"from rod",from_rod,"to rod",to_rod 
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
          
# Driver code 
n = 4
TowerOfHanoi(n, \'A\', \'C\', \'B\') 

             
             C:\Users\Your Name>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
