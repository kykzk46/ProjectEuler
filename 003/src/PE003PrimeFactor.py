import math

def LargestPrimeFactor(n_target):
    factor = []
    n=n_target
    last_i = 0

    while(True):
        if n%2 == 0:
            n = n//2
            factor.append(2)

        up_limit = math.ceil( math.sqrt(n))
        for i in range(3,up_limit,2):
            if(n%i == 0):
                n = n//i
                factor.append(i)
                break;
            else:
                last_i = i

        if(last_i == math.ceil(math.sqrt(n_target))):
            factor.append(n_target)
            break;
        elif(last_i == up_limit):
            break;

    return factor.pop



if __name__ == '__main__':
    with open('../data/input/input00.txt', 'r') as fileObj:
        t = int(fileObj.readline())
        for case in range(0, t, 1):
            n = int(fileObj.readline())

            rst = LargestPrimeFactor(n)

            print(rst)
