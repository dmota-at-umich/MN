import numpy as np

from LUs import *

a = np.array([[ 3.0, -1.0, 4.0], [-2.0, 0.0, 5.0],\
              [ 7.0, 2.0, -2.0]]) 
b = np.array([[ 6.0, 3.0, 7.0],[-4.0, 2.0, -5.0]]) 
a = LU(a)

print('Matriz modificada: ',a)

det = np.prod(np.diagonal(a))

print("\nDeterminante =",det)

#sustitucion regresiva
for i in range(len(b)): 
   x = LUsol(a,b[i])
   print("x",i+1,"=",x)

