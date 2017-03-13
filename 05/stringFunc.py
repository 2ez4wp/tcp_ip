# coding: utf-8
import sys
import re 
def stringFunc(filename):
    with open(filename,'rb') as f:
        reader = f.read()
        print reader
        print len(reader)
        pattern1 = re.compile('\n')
        text01 = pattern1.sub('',reader)
        pattern2 = re.compile('2012')
        text02 = pattern2.sub('2017',reader)
        with open('./test01.txt','wb') as ff:
            ff.write(text01)
        with open('./test02.txt','wb') as fff:
            fff.write(text02)
        pattern3 = re.findall(r'[0-9]+',reader)
        print pattern3
        
         
if __name__=="__main__":
    if len(sys.argv) < 2:
        filename = "./test.txt"
    else:
        filename = sys.argv[1]
    stringFunc(filename)
    
