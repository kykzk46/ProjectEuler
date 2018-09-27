from decimal import *

def cal_sum_multiple(n_max, multiple):
    start = 0
    # range(1,6,1) is [1,2,3,4,5]
    for i in range(1, multiple+1, 1):
        if (n_max-i) % multiple == 0:
            start = n_max-i
            break
        
    # let start = w * multiple
    # 0 + multiple + 2*multiple + ... + w*multiple
    # = (0+1+2+...+w)*multiple
    # = (w(w+1)/2)*multiple
    # = (start/multiple) * ((start/multiple)+1) * (multiple/2)
    getcontext().prec = 16
    return  Decimal(start * start / multiple + start ) /2 


if __name__ == '__main__':
    with open('./data/input/input05.txt', 'r') as fileObj:
        t = int(fileObj.readline())
        for case in range(0, t, 1):
            n = int(fileObj.readline())

            # Sum of multiple of 3 below n
            sum_of_multiple3 = cal_sum_multiple(n, 3)
            # Sum of multiple of 5 below n
            sum_of_multiple5 = cal_sum_multiple(n, 5)
            # Bcz the sum of (3 * 5) will be added twice, remove them
            sum_of_multiple15 = cal_sum_multiple(n, 15)

            sum = sum_of_multiple3 + sum_of_multiple5 - sum_of_multiple15

            print(int(sum))












