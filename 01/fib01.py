# coding: utf-8
import sys
def fib(num = 8):
    if num == 1:
        return 1
    if num == 2:
        return 1
    else :
        return fib(num-1) + fib(num-2)
if __name__ == '__main__':
    list = []
    if len(sys.argv) < 2:
        for n in range(8):
            list.append(fib(n+1))
        print list
    elif sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
        for n in range(int(sys.argv[1])):
            list.append(fib(n+1))
        print list
    else:
        print "input error!"
