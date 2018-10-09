import math
import os

def LargestPrimeFactor(n_target):
    factor = []
    n=n_target
    last_i = 0


    while(True):
        if n%2 == 0:
            n = n//2
            factor.append(2)
            continue

        # bcz the for loop can't handle n < 9 properly
        if n < 9 :
            if n == 1:
                break
            elif n == 3:
                factor.append(3)
                break
            elif n == 5:
                factor.append(5)
                break
            elif n == 7:
                factor.append(7)
                break

        up_limit = math.ceil( math.sqrt(n))
        if up_limit%2 == 0:
            up_limit += 1 # ensure this loop can be exited

        for i in range(3,up_limit+2,2): # bcz range(1,5,2) = [1, 3] only
            last_i = i
            if(n%i == 0):
                n = n//i
                factor.append(i)
                break;

        
        if(last_i == up_limit): # no factor in [3,5,...,uplimit]
            factor.append(n)
            break;
            
    #print(factor)
    factor.sort()
    return factor.pop()



if __name__ == '__main__':
    with open('../data/input/input00.txt', 'r') as fileObj:
        t = int(fileObj.readline())
        for case in range(0, t, 1):
            n = int(fileObj.readline())

            rst = LargestPrimeFactor(n)

            print(rst)
