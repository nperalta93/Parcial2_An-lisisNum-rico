import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def politaylor(funcionx,x0,n):
    i = 0
    p = 0
    while i <= n:
        derivada = funcionx.diff(x,i)
        derivadax0 = derivada.subs(x,x0)
        divisor = np.math.factorial(i)
        ti = (derivadax0/divisor) * (x-x0)**i
        p = p + ti
        i = i + 1
    return (p)

# PROGRAMA

x = sp.Symbol('x')
funcionx = (x**6/84)-(3cos(2x)/8)

x0 = 0
xi = 3*0,2
n = 3 

# PROCEDIMIENTO
polinomio = politaylor(funcionx,x0,n)
px = polinomio.subs(x,xi)
fx = funcionx.subs(x,xi)
ereal = fx-px

print('Error general: ',ereal)