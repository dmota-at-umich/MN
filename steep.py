## module steep

import numpy as np
import math

def steep(Av,x,b,kmax=1e3,tol=1.0e-9):
    r = b - Av(x)
    s = r.copy()
    y = np.copy(x)
    k = 1
    for i in range(int(kmax)):
        u = Av(s)
        alpha = np.dot(s.T,r)/np.dot(s.T,u)
        x = x + alpha*r
        r = r - alpha*u
        y = np.hstack([y,x])
        k += 1
        if(math.sqrt(np.dot(r.T,r))) < tol:
            break
        s = r.copy()
    return x, k, y


A=np.array([[3.,2.],[2.,6.]])    
b=np.array([[5.],[8.]])
x=np.array([[0.],[.0]])

def Av(x):
    return A@x
    
x,k,y=steep(Av,x,b,tol=1.0e-9)

print("sol=",x)
print("iter=",k)



