# coding: utf-8
import sys
import math
def numbers(num = 10):
   list = []
   if num <= 1:
       return False
   if num == 2:
       return True
   if num == 3:
       return True
   num_2 = int(math.sqrt(num))
   for i in range(2,num_2+1):
       if num % i == 0:
            return False
   return True 
   #return list
   
   
if __name__ == "__main__":
    if len(sys.argv) < 2:
        num = 10
    else:
        num = sys.argv[1]
    for i in range(int(num)):
        #print i
        if numbers(i+1) == True:
             print i+1
                
