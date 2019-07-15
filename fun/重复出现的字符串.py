"""
给出一个非空的字符串，
判断这个字符串是否是由它的一个子串进行多次首尾拼接构成的。
例如，"abcabcabc"满足条件，因为它是由"abc"首尾拼接而成的，而"abcab"则不满足条件。
"""
import sys
line=sys.stdin.readline().strip()
l=len(line)
def getRes(l):
    for i in range(1,l//2+1):
        if l%i!=0:
            continue
        else:
            num_sub=l//i
            init=line[:i]
            for k in range(1,num_sub+1):
                if init != line[k*i:(k+1)*i]:
                    break
            if num_sub==k:
                return init
    return False

print(getRes(l))