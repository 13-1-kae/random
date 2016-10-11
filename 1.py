__author__ = 'student'
import matplotlib.pyplot as plt
import random as rd
n1=100
n2=1000
n3=10000
n4=100000
rd.seed(0)
plt.subplot(221)
values1 = [rd.normalvariate(0, 1) for i in range(n1)]
plt.hist(values1, bins=100)
plt.subplot(222)
values2 = [rd.normalvariate(0, 1) for i in range(n2)]
plt.hist(values2, bins=100)
plt.subplot(223)
values3 = [rd.normalvariate(0, 1) for i in range(n3)]
plt.hist(values3, bins=100)
plt.subplot(224)
values4= [rd.normalvariate(0, 1) for i in range(n4)]
plt.hist(values4, bins=100)
plt.show()
