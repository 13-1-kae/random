__author__ = 'student'
import numpy as np
import random as rd
import matplotlib.pyplot as plt
def get_p(a,b):
    c=b*[0]
    for i in range (b):
        p=i/b*100
        if p==0:
            c[i]=0.0
        else:
            c[i]=np.percentile(a, p)
    return(c)
def get_p_n(x, y):
    z=0.0
    for i in range (len(y)):
        if x>=y[i]:
            z=i
    return(z)
def v_e(a, b, a_r=False):
    idx=get_p_n(a, b)
    step=1/len(b)
    if a_r==True:
        return(idx*step+rd.uniform(0, step))
    else:
        return(idx*step)

def v_e1(a, b, a_r=False):
    c=[0]*len(a)
    for i in range (len(a)):
        idx=get_p_n(a[i], b)
        step=1/len(b)
        if a_r==True:
            c[i]=idx*step+rd.uniform(0, step)
        else:
            c[i]=idx*step
    return(c)
A=[]
with open('img.txt', 'r') as f:
    for line in f:
        v=list(map(float, line.strip().split()))
        A.append(v)
data=np.array(A)
plt.imshow(data, cmap = plt.get_cmap('gray'))


