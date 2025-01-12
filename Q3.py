import numpy as np
A = np.array(
    [ 
        [3,4,3], 
        [1,2,3], 
        [4,2,1]
    ] 
) 

#performing SVD 
U, S, V = np.linalg.svd(A) 
print(U) 
print(V) 
print(S) 