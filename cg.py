## module cg

import numpy as np
import math
import rogues as rg

def cg(Av,x,b,tol=1.0e-9):
    n = len(b)
    r = b - Av(x)
    s = r.copy()
    for i in range(n):
        u = Av(s)
        alpha = np.dot(s.T,r)/np.dot(s.T,u)
        x = x + alpha*s
        r = b - Av(x)
        if(math.sqrt(np.dot(r.T,r))) < tol:
            break
        else:
            beta = -np.dot(r.T,u)/np.dot(s.T,u)
            s = r + beta*s
    return x,i


A=rg.prolate(30)    
b=A@np.ones((30,1))
x0=np.zeros((30,1))
##
def Av(x):
    return A@x
##    
x,i=cg(Av,x0,b,tol=1.0e-9)
##
print("sol=",x)
print("error=",np.linalg.norm(x-np.ones((30,1)))/np.linalg.norm(np.ones((30,1))))
print("iter=",i)
##


