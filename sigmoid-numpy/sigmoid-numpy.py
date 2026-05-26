import numpy as np
import math

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here

    if type(x) == int:
        return 1/(1+np.exp(-1*x)) 

    if type(x) == list and type(x[0]) == list:
        return [[1/(1+np.exp(-1*a)) for a in b] for b in x ]
    
    return [1/(1+np.exp(-1*a)) for a in x]

    