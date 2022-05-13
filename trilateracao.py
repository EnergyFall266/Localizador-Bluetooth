import numpy as np
from sympy import Matrix

x1 = int(input("valor de x1: "))
x2 = int(input("valor de x2: "))
x3 = int(input("valor de x3: "))
y1 = int(input("valor de y1: "))
y2 = int(input("valor de y2: "))
y3 = int(input("valor de y3: "))
d1 = int(input("distancia beacon 1: "))
d2 = int(input("distancia beacon 2: "))
d3 = int(input("distancia beacon 3: "))

A1 = 2*(x2-x1)
A2 = 2*(x3-x1)
A3 = 2*(x3-x2)

B1 = 2*(y2-y1)
B2 = 2*(y3-y1)
B3 = 2*(y3-y2)

C1 = np.power(d1,2) - np.power(d2,2) + np.power(x2,2) - np.power(x1,2) + np.power(y2,2) - np.power(y1,2)
C2 = np.power(d1,2) - np.power(d3,2) + np.power(x3,2) - np.power(x1,2) + np.power(y3,2) - np.power(y1,2)
C3 = np.power(d2,2) - np.power(d3,2) + np.power(x3,2) - np.power(x2,2) + np.power(y3,2) - np.power(y2,2)

Mtr0 = np.array([[np.power(A1,2)+np.power(A2,2)+np.power(A3,2), A1*B1+A2*B2+A3*B3],
                [A1*B1+A2*B2+A3*B3, np.power(B1,2)+np.power(B2,2)+np.power(B3,2)]])

Mtr1 = Mtr0.transpose()

Mtr2 = np.array([[A1*C1+A2*C2+A3*C3],
                [B1*C1+B2*C2+B3*C3]])
coordenadas = np.dot(Mtr1,Mtr2)


