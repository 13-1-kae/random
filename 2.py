__author__ = 'student'
import random as rd
a=-3
b=3
n=10000000
s=0
for i in range(n):
    x=rd.uniform(a, b)
    if abs(x)<=2:
        f=-x**2+4
    else:
        f=0
    s+=f
s=s*(b-a)/n
print(s)