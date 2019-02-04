import math
import os
from os import path

# largest 3-dig number is 999, smallest 6-dig number is 100000
# 100000 / 999 = 100.1
# ==> we should search between 101 to 999
def Find3DigProduct(n):
    factor = 999
    while(factor > 100):
        if(n % factor == 0):
            if((n // factor) < 1000):
                return True
        
        factor = factor - 1

    return False



# Stupid way!
# we know the input should have 6 digit
def CheckIfPalindrome(n):
    d6 = n//100000
    d5 = (n - d6 * 100000) // 10000
    d4 = (n - d6 * 100000 - d5 * 10000) // 1000
    d3 = (n - d6 * 100000 - d5 * 10000 - d4 * 1000) // 100
    d2 = (n - d6 * 100000 - d5 * 10000 - d4 * 1000 - d3 * 100 ) // 10
    d1 = (n - d6 * 100000 - d5 * 10000 - d4 * 1000 - d3 * 100 - d2 * 10)

    isPalindrome = True
    isPalindrome = isPalindrome and d6 == d1
    isPalindrome = isPalindrome and d5 == d2
    isPalindrome = isPalindrome and d4 == d3

    return isPalindrome

############################################################################################
# Smart way: convert the number to string and reverse it then compare with the original one
############################################################################################



def FindLargestPalindromeProductSmallerThan(n_target):
    n=n_target

    while(True):
        n = n-1
        if(CheckIfPalindrome(n)):
            if(Find3DigProduct(n)):
                break
        
    return n



if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    print(os.getcwd())
    print("=============================================")


    input_path = os.path.normpath(os.path.join(dir_path, "data\input\input00.txt"))
    with open(input_path, 'r') as fileObj:
        t = int(fileObj.readline())
        for case in range(0, t, 1):
            n = int(fileObj.readline())

            rst = FindLargestPalindromeProductSmallerThan(n)

            print(rst)
