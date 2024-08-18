![example workflow](https://github.com/mazhar-ansari-ardeh/BenchmarkFcns/actions/workflows/build.yaml/badge.svg)
[![Downloads](https://static.pepy.tech/badge/benchmarkfcns)](https://pepy.tech/project/benchmarkfcns)

# BenchmarkFcns
Benchmarkfcns is an effort to provide a high-perfomant, public and free implementation of well-known benchmark functions for mathematical optimization algorithms in Python. The Python library is implemented in C++ and utilizes the powerful SIMD vector calucluations to offer very fast and efficient evaluation of the implemented functions on large batches of data.

For the documentation of the implemented functions and their features, please visit [https://benchmarkfcns.info](https://benchmarkfcns.info).

# How to use
## Python
### Installation
The library is packaged and available on the PyPI index. To install, simply run `pip install benchmarkfcns`.

### Usage
After installing, using the library is straightforward and all that is needed is to import the needed functions, construct a matrix of input values and call the function.
It should be noted that all the functions in the library only accept matrices as input. The rows of the matrix represent the data points at which the function should be evaluated and the columns represent the dimensions of data points. The code snippet shows how to use the library.

```python
# Import the needed function.
from benchmarkfcns import rastrigin
import numpy as np

# Look at the function's documentation.
print(rastrigin.__doc__)

# The input matrix can be list of lists.
data = [[0, 0, 0]]

# Evaluate the Rastrigin function at (0, 0, 0).
results = rastrigin(data)
print(results)

# The input can also be a Numpy matrix.
data = np.array([[0, 0, 0], [1, 1, 1]])
results = rastrigin(data)
print(results)
```

### Plotting the functions
This library is implemented to be as compatible as possible with all the mainstream plotting libraries. As a result, you are free to select your favourite plotting library to plot the functions in this library.

Plotting a mathematical function like `rastrigin` requires evaluating the function at a rather large set of data points. This is where the vectorized implementation of the functions in this package can shine as it allows performing the evaluations in a single function call, which significantly speeds up the plotting and reduces the computation cost. To facilitate this, the library also contains a helper function, `meshgrid`, for drawing 3D plots using the vectorized implemetations of the mathematical functions in this library. Given a list of *x* and *y* coordinates and a function, this function creates a meshgrid of points, evaluates the function over the meshgrid and returns the corresponding *x*, *y* and *z* points of the meshgrid that can be plotted with any plotting library.

```python
from benchmarkfcns import ackley
from benchmarkfcns.plotting import meshgrid

# Using the matplotlib library for this example
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# We want to plot the function for x and y in range [-5, 5].
# This corresponds to a grid of 10,000,000 points.
x = np.linspace(-5, 5, 10000)
y = np.linspace(-5, 5, 10000)

# `meshgrid` creates the 3D meshgrid and evaluates `ackley` on it.
# Evaluation of 100,000,000 points took less than 3 seconds.
X, Y, Z = meshgrid(x, y, ackley)

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface and its contour with a colormap
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
ax.contour(X, Y, Z, zdir='z', offset=0, cmap='coolwarm')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()
```

<p align="center">
    <img src="https://raw.githubusercontent.com/mazhar-ansari-ardeh/BenchmarkFcns/master/image-1.png" alt="drawing" width="700"/>
</p>

## MATLAB
As a reference, the repository also contains the implementation of the functions in MATLAB. To install and use the MATLAB implementation, it is just required to add the project folders to MATLAB's path. For example, to use the functions in the 'benchmarks/MATLAB' folder, just navigate to this folder with MATLAB's directory explorer or use the command `addpath` with path to the folder on your PC (e.g. `addpath /path/to/benchmarks`).

# Local development and compilation
The library is built with the [pybind11](https://pybind11.readthedocs.io/), [scikit-build-core](scikit-build-core) and [Eigen](https://eigen.tuxfamily.org/) libraries. To compile the library, you will need to have CMake version 3.15 or above installed and configured. The easiest way to compile and install the package locally is to clone the repository into a directory, e.g. `BenchmarkFcns`, and then run `pip install ./BenchmarkFcns`. Although optional, it is highly recommended to install the package into a virtual environment.

# Contribution
Any suggestions and contributions are welcomed. The best way to contribute to the library is to fork the repository, apply the contributions and create a pull request.

# Support
Any bug reports, code contributions, suggestions, feedback and insights are greatly appreciated. If you are using this library in a research publication, please kindly consider citing the repository as "Ardeh, M. A. [2024] BenchmarkFcns [Source Code]. GitHub. https://github.com/mazhar-ansari-ardeh/BenchmarkFcns".
