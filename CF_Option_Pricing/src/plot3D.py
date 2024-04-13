import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plot3D:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z


    def plot(self, title="ImplyVolSurface", X_label='Times', Y_label='Log_Moneyness', Z_label='Imply_Vol'):
        X, Y = np.meshgrid(self.X, self.Y)
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, self.Z, cmap='viridis')
        ax.set_title(title)
        ax.set_xlabel(X_label)
        ax.set_ylabel(Y_label)
        ax.set_zlabel(Z_label)

        ax.yaxis.labelpad = 15
        plt.show()

# Generate data
# x = np.linspace(-1, 1, 100)
# y = np.linspace(-1, 1, 100)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(3 * np.sqrt(X**2 + Y**2))

# Plot the surface
