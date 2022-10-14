import numpy as np  
x = np.arange(12).reshape(3,2,2).swapaxes(1,2)  
x  
y=np.ravel(a, order='C')  
y  
z=np.ravel(a, order='K')  
z  
q=np.ravel(a, order='A')  
q  
