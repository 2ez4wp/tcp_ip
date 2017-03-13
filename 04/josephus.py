# coding: utf-8
import sys
import math 
def josephus(N = 6,M = 5):
    out = []
    list = range(1,N+1)
    m = M - 1
    out.append(list[m])
    list.remove(list[m])
    while(len(list) > 0):
        # list.remove(list[m])
        N = len(list)
        m = (m + M - 1) % N
        out.append(list[m])
        list.remove(list[m])
    print out
    
if __name__=="__main__":
    if len(sys.argv) < 2:
        josephus()
    elif sys.argv[1].isdigit() and int(sys.argv[1]) > 0 and sys.argv[2].isdigit() and int(sys.argv[2]) > 0:
        josephus(int(sys.argv[1]),int(sys.argv[2]))
        
