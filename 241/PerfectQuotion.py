import math
import os
from os import path
import numpy as np

def FindSmallestDivisor(oddNumber, startFrom, endBefore):
    upLimit = math.floor(math.sqrt(oddNumber))
    if(endBefore < upLimit):
        upLimit = endBefore
    
    for i in range (startFrom, upLimit + 1, 2):
        if oddNumber % i == 0:
            return i
    return 1



def TestPerfectQuotion(k):

    sum = 1 + k
   
    # Find divisors that are power of 2
    j = k
    powOf2 = 1
    ed_list = []
    while (j / 2)  % 2 == 0:
        j = j / 2
        powOf2 *= 2
        ed_list.append(powOf2)
        sum += powOf2 + j
        
    # first odd divisor encounter
    powOf2 *= 2
    j = j / 2 
    sum += j + powOf2
    ed_list.append(powOf2)
    
    #print(ed_list)

    # Find other odd divisor
    oddDivisor = j
    od_list = []
    upLimit = math.ceil(math.sqrt(k))
    startFrom = 3
    endBefore = math.ceil(math.sqrt(oddDivisor))
    while(True):
        o1 = FindSmallestDivisor(oddDivisor, startFrom, endBefore) 
        if(o1 == 1): 
            break
        o2 = oddDivisor / o1
   
        temp = [o1, o2]
        for o in od_list:
            temp.append(o * o1)
            temp.append(o * o2)
       
        for t in temp:
            if(t not in od_list and t < upLimit):
                od_list.append(t)

        oddDivisor = o2
        startFrom = o1
        endBefore = o2


    # Form other even divisors
    other_list = []
    for d in ed_list:
        for o in od_list:
            p = d * o
            if p < upLimit : 
                other_list.append(p)

    if len(od_list) > 0:
        for d in od_list:
            sum += d + k/d
    
    if len(other_list) > 0:
        for d in other_list:
            sum += d + k/d

    PQ = sum / k
    return PQ;


def TestPerfectQuotion2(k):

    sum = 1 + k
    sum += 2 + k/2
   
    upLimit = math.floor(math.sqrt(k))
    for i in range (3,upLimit+1,1):
        if k % i == 0:
            sum += i + k / i
            print(i)
    
    PQ = sum / k
    return PQ;



"""
Find n <= 1E23, such that n has perfect quotion 
"""
if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    print(os.getcwd())
    print("=============================================")


    input_path = os.path.normpath(os.path.join(dir_path, "data\input\input00.txt"))
    with open(input_path, 'r') as fileObj:
        q= int(fileObj.readline())
        print(q)

        for k in range(10, 10000000 + 1, 2): # n must be even
            PQ = TestPerfectQuotion(k)
            if(math.fmod(PQ * 2 - 1, 2) == 0):
                print("{0}, {1}".format(k, PQ))

