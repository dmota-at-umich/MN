## module jacobi

import numpy as np

def jacobi(A,b,x0,kmax,tol=1.0e-9):
    n=A.shape[0]
    x=np.zeros((n,1))
    y=np.copy(x0)
    k=1
    r=b-A@x0
    r0=np.copy(r)

    while np.sqrt(np.dot(r.T,r))>tol*np.sqrt(np.dot(r0.T,r0)) and (k<kmax):
            for i in range(n):
                x[i]=(b[i]-A[i,:i]@x[:i]-\
                      A[i,i+1:]@x0[i+1:])/A[i,i]

            r=b-A@x
            x0=np.copy(x)
            y=np.hstack([y,x])
            k=k+1
    return x,k,y

A=np.array([[3.,2.],[2.,6.]])    
b=np.array([[5.],[8.]])
x0=np.array([[0.],[0.]])

# def Av(x):
#     return A@x
    
x,k,y=jacobi(A,b,x0,1e2,tol=1.0e-9)

print("sol=",x)
print("iter=",k)