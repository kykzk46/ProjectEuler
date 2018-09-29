def SumEvenFibonacci(n_max):
    f_im2 = 1 # f(0)
    f_im1 = 1 # f(1)
    f_i = f_im1 + f_im2 # f(2)

    if n_max < 3:
        return 0
    else:
        s = f_i

    # from 1 to n_max is obvious larger than we need
    for k in range(1,n_max,1):
        f_i1 = f_i  + f_im1 # f(3k)
        f_i2 = f_i1 + f_i    # f(3k+1)
        f_i3 = f_i2 + f_i1   # f(3k+2)

        if f_i3 > n_max:
            break
        else:
            s += f_i3
            f_i = f_i3
            f_im1 = f_i2

    return s



if __name__ == '__main__':
    with open('../data/input/input04.txt', 'r') as fileObj:
        t = int(fileObj.readline())
        for case in range(0, t, 1):
            n = int(fileObj.readline())

            rst = SumEvenFibonacci(n)
            print(rst)
