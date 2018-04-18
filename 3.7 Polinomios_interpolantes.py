import numpy as np
from scipy.interpolate import barycentric_interpolate
def runge(x):
    """Función de Runge."""
    return 1 / (1 + 25*x ** 2)
N = 3  # Nodos de interpolación
xp = array ([5,10,20])
fp = runge(xp)
x = np.linspace(0, 20)
y = barycentric_interpolate(xp, fp, x)
