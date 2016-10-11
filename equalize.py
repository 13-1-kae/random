__author__ = 'student'
import numpy as np
import random as rd
import matplotlib.pyplot as plt
def get_percentile(a,b):
    c=b*[0]
    for i in range (b):
        p=i/b*100
        if p==0:
            c[i]=0.0
        else:
            c[i]=np.percentile(a, p)
    return(c)
def get_percentile_number(x, y):
    z=0.0
    for i in range (len(y)):
        if x>=y[i]:
            z=i
    return(z)
def value_equalization(a, b, add_random=False):
    idx=get_percentile_number(a, b)
    step=1/len(b)
    if add_random==True:
        return(idx*step+rd.uniform(0, step))
    else:
        return(idx*step)

def values_equalization(a, b, add_random=False):
    c=[0]*len(a)
    for i in range (len(a)):
        idx=get_percentile_number(a[i], b)
        step=1/len(b)
        if add_random==True:
            c[i]=idx*step+rd.uniform(0, step)
        else:
            c[i]=idx*step
    return(c)
if __name__=='__main__':
    A=[]
    with open('img.txt', 'r') as f:
        for line in f:
            v=list(map(float, line.strip().split()))
            A.append(v)
    data=np.array(A)
    plt.subplot(221)
    plt.imshow(data, cmap = plt.get_cmap('gray'))
    plt.subplot(222)
    v=data.flatten()
    plt.hist(v, bins=100)
    h=values_equalization(v, get_percentile(v,), add_random=True)
    new_data = h.reshape((200, 267))
    plt.subplot(223)
    plt.imshow(new_data, cmap = plt.get_cmap('gray'))