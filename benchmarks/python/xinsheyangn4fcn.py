import numpy as np

def xinsheyangn4fcn(x: np.ndarray) -> np.ndarray:
    """
    Computes the value of the Xin-She Yang N. 4 function.
    
    Parameters:
    -----------
    x (numpy.ndarray): input matrix of size M-by-N
    
    Returns:
    --------
    numpy.ndarray: A vector of size M-by-1 in which each row contains the 
                    function value for the corresponding row of X.
    
    Author: Mazhar Ansari Ardeh
    Please forward any comments or bug reports to mazhar.ansari.ardeh at
    Google's e-mail service or feel free to kindly modify the repository.
    """
    scores = (np.sum(np.sin(x) ** 2, axis=1) - np.exp(-np.sum(x ** 2, axis=1))) * np.exp(-np.sum(np.sin(np.sqrt(np.abs(x))) ** 2, axis=1))
    return scores
