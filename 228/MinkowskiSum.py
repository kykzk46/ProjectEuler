import math
import os
from os import path
import numpy as np
import matplotlib.pyplot as plt

def Visualize(n):
    vertexes = np.zeros((n+1,2))
    for k in range(0,n,1):
        vertexes[k,0] = np.cos((2*k-1)*np.pi / n)
        vertexes[k,1] = np.sin((2*k-1)*np.pi / n) 

    # for plotting purpose, the last index (extra one) is the same as the first
    vertexes[n,:] = vertexes[0,:]

    plt.plot(vertexes[:,0], vertexes[:,1], marker = 'o')
    plt.show()
    return 0



def VisualizeSum(start, end):

    for n in range(start, end, 1):
        small = n
        large = n+1


        n_small = small 
        vertexes_small = np.zeros((n_small+1,2))
        for k in range(0,n_small,1):
            vertexes_small[k,0] = np.cos((2*k-1)*np.pi / n_small)
            vertexes_small[k,1] = np.sin((2*k-1)*np.pi / n_small)
        vertexes_small[n_small,:] = vertexes_small[0,:]
        plt.plot(vertexes_small[:,0], vertexes_small[:,1], marker = 'o')
        
        
        n_large = large 
        vertexes_large = np.zeros((n_large+1,2))
        for k in range(0,n_large,1):
            vertexes_large[k,0] = np.cos((2*k-1)*np.pi / n_large)
            vertexes_large[k,1] = np.sin((2*k-1)*np.pi / n_large)
        vertexes_large[n_large,:] = vertexes_large[0,:]
        plt.plot(vertexes_large[:,0], vertexes_large[:,1], marker = 'o')


        n_mSum = n_small * n_large
        vertexes_mSum = np.zeros((n_mSum +1, 2))
        idx = 0
        for i in range(0, n_small, 1):
            for j in range(0, n_large, 1):
                vertexes_mSum[idx,0] = vertexes_small[i,0] + vertexes_large[j,0]
                vertexes_mSum[idx,1] = vertexes_small[i,1] + vertexes_large[j,1]
                idx = idx + 1
        vertexes_mSum[n_mSum,:] = vertexes_mSum[0,:]

        #print(vertexes_mSum[:,0])
        plt.scatter(vertexes_mSum[:,0], vertexes_mSum[:,1], marker = 'D')

        plt.axis([-2,2,-2,2])
        plt.show()
    return 0













"""
Observe that the smallest multiple of [1,2,...,N] must be a product 
of all prime number within [1,2,...,N]
"""
if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    print(os.getcwd())
    print("=============================================")


    input_path = os.path.normpath(os.path.join(dir_path, "data\input\input00.txt"))
    with open(input_path, 'r') as fileObj:
        q= int(fileObj.readline())
        for case in range(0, q, 1):
            strInput = str(fileObj.readline()).split(' ')
            l = int(strInput[0])
            r = int(strInput[1])
            print(l,r)

            #Visualize(l)
            #Visualize(r)


            VisualizeSum(l,r)

            #print(rst)
