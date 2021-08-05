import numpy as np

def SIDN(weight,bias,**dynm):
    sum = []
    for i in dynm:
        #print(dynm[i])
        for j in range(len(dynm[i])):
            if j==0:
                dynm[i][j] = np.append(dynm[i][j],0) #initial inout zero
                sum.append(weight.dot(dynm[i][j])+bias)
                
            else:
                dynm[i][j]  = np.append(dynm[i][j],dynm[i][j-1][0])
                sum.append([weight.dot(dynm[i][j])+bias])
                

    print(sum)

if __name__ == "__main__": 
    
    bias = 0
    w = np.array([[1,2]] )
    p1 = np.array([1])
    p2 = np.array([2])
    p3 = np.array([3])
    p4 = np.array([4])
    
    SIDN(weight=w,bias=bias,dynm=[p1,p2,p3,p4])