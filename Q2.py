# import numpy library 
import numpy as np  # type: ignore
  
# initialize X and Y matrices 
X = np.array([[1,2,3], 
              [2,5,6], 
              [1,2,1]]) 
Y = np.array([[-5, 5,-10], 
              [ 1, 2, 8], 
              [ 5, 4, 1]]) 
  
# perform cross-product using @ 
Z = np.cross(X ,Y ) 
  
# print the resulting matrix 
print(Z)