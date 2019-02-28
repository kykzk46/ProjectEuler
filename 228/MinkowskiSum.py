import math
import os
from os import path

from bisect import bisect_left as bl
from functools import reduce

def FindAllPrimeWintin(n_upbound):
    arr = [2]
    isPrime = True
    for i in range(3,n_upbound+1,2):
        for j in range (3,i,1):
            if(i % j == 0):
                isPrime = False
                break
        if(isPrime):
            arr.append(i)
        isPrime = True
    
    return arr


def FindSmallestMultiple(n_target, primeArr):
    intersec = bl(primeArr, n_target)
    primeArrWithin = [val for val in primeArr[0:intersec+1] if val <= n_target]
    if(len(primeArrWithin) == 0):
        return 1
    primeProduct = reduce((lambda x,y: x*y), primeArrWithin)
    
    
    counter = 0
    p = primeProduct
    allDivisible = False
    while(not allDivisible):
        counter += 1
        p = primeProduct * counter
        allDivisible = True
        for j in range (2,n_target+1,1):
            if(p % j != 0):
                allDivisible = False
                break

    return p


"""
Observe that the smallest multiple of [1,2,...,N] must be a product 
of all prime number within [1,2,...,N]
"""
if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    print(os.getcwd())
    print("=============================================")


    input_path = os.path.normpath(os.path.join(dir_path, "data\input\input04.txt"))
    with open(input_path, 'r') as fileObj:
        t = int(fileObj.readline())
        for case in range(0, t, 1):
            n = int(fileObj.readline())

            upbound = 40
            rst = FindSmallestMultiple(n, FindAllPrimeWintin(upbound))

            print(rst)
