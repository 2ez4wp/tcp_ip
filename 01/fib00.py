# coding: utf-8
import sys
def fibo(num = 8):
    end = num
    list = []
    x,y = 1,1
    list.append(x)
    list.append(y)
    while(num - 2  > 0):
        list.append(list[-1]+list[-2])
        num = num - 1
    print list[:end]
if __name__ == '__main__':
    num = raw_input("input: num\n")
    fibo(int(num)) 
        
