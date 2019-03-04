import math
import os
from os import path
import numpy as np
import matplotlib.pyplot as plt

def CalculateVertex(n):
    vertexes = np.zeros((n+1,4))

    for k in range(1,n+1,1):
        vertexes[k,3] = phi = (2*k-1)*180 / n
        vertexes[k,0] = np.cos(phi * np.pi / 180)
        vertexes[k,1] = np.sin(phi * np.pi / 180) 
        vertexes[k,2] = np.sqrt(vertexes[k,0] * vertexes[k,0] + vertexes[k,1] * vertexes[k,1])

    # for plotting purpose, the first index (extra one) is the same as the last 
    vertexes[0,:] = vertexes[n,:]
    return vertexes


def CalculateMinkowskiSum(n1, vtx1, n2, vtx2):
    n_mSum = n1 * n2
    vtx_rst = np.zeros((n_mSum +1, 4))
    idx = 1
    for i in range(1, n1+1, 1):

        r1_sqr = vtx1[i,0] * vtx1[i,0] + vtx1[i,1] * vtx1[i,1]
        r1 = np.sqrt(r1_sqr)
        phi1 = vtx1[i,3]

        for j in range(1, n2+1, 1):
            vtx_rst[idx,0] = vtx1[i,0] + vtx2[j,0]
            vtx_rst[idx,1] = vtx1[i,1] + vtx2[j,1]

            r2_sqr = vtx2[j,0] * vtx2[j,0] + vtx2[j,1] * vtx2[j,1]
            r2 = np.sqrt(r2_sqr)
            phi2 = vtx2[j,3]

            # radius
            phi_minus = (phi2-phi1)*np.pi/180 
            vtx_rst[idx,2] = np.sqrt( r1_sqr + r2_sqr + 2 * r1 * r2 * np.cos(phi_minus) )
            # angle
            vtx_rst[idx,3] = phi1 +  np.arctan2( r2*np.sin(phi_minus), r1 + r2*np.cos(phi_minus) ) * 180 / np.pi

            # x, y check
            x = vtx_rst[idx,2] * np.cos(vtx_rst[idx,3]*np.pi / 180)
            y = vtx_rst[idx,2] * np.sin(vtx_rst[idx,3]*np.pi / 180)

            idx = idx + 1
    vtx_rst[0,:] = vtx_rst[n_mSum,:]
    return vtx_rst


def FindNextVertexes(vtx_in, plt):
    row = vtx_in.shape[0] - 1 # exclude the extra first index
    
    idx_total = int((row+1)/2) 
    vtx = vtx_in[1:idx_total +1 ,:]

    vtx_new = vtx[vtx[:,2].argsort()[::-1]] # [::-1] do a reverse 
    
    for i in range(0, idx_total-2, 1):
        x= [vtx_new[i,0],vtx_new[i+1,0]]
        y= [vtx_new[i,1],vtx_new[i+1,1]]
        plt.plot(x,y)

    
    vtx_rst = vtx


    return vtx_rst




def VisualizeSum(start, end):

    for n in range(start, end, 1):
        n_small = n
        n_large = n+1

        vertexes_small = CalculateVertex(n_small) 
        plt.plot(vertexes_small[:,0], vertexes_small[:,1], marker = 'o')
        
        vertexes_large = CalculateVertex(n_large) 
        plt.plot(vertexes_large[:,0], vertexes_large[:,1], marker = 'o')


        vertexes_mSum = CalculateMinkowskiSum(n_small, vertexes_small, n_large, vertexes_large)
        print(vertexes_mSum)
        plt.scatter(vertexes_mSum[:,0], vertexes_mSum[:,1], marker = 'D')

        vert_next = FindNextVertexes(vertexes_mSum, plt)


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
