# coding: utf-8
import sys
import re
def stringfun2(string):
    pattern1 = re.compile('\d')
    new_string = pattern1.findall(string)
    print new_string
    new_str = string.lower()
    new_dir = {}
    pattern2 = re.compile(r'[a-z]',re.I)
    pattern3 = re.compile(r'[a-z0-9]')
    list1 = pattern2.findall(new_str)
    list2 = pattern3.findall(new_str)
    #print list1
    print list2
    for i in range(len(list1)):
        new_dir[list1[i]] = list1.count(list1[i])
    print new_dir
    items = new_dir.items()
    print items.sort()
    
    
    
if __name__ == "__main__":
    string = "aAsmr3idd4bgs7Dlsf9eAF"
    stringfun2(string)
   
