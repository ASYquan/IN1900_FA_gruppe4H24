import matplotlib.pyplot as plt 
import numpy as np

def f(x):
    return np.log(x)

def wompwomp(x):
    return x

def wompwomp1(x):
    return x*np.log(x)

Df = np.linspace(0,1000000000000000, 10)

plt.plot(Df, f(Df))
plt.plot(Df, wompwomp(Df))
plt.plot(Df, wompwomp1(Df))
plt.show() 
