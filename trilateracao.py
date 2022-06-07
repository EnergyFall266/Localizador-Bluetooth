from cmath import log10
from turtle import distance
import numpy as np
from sympy import Matrix

x1 = 0
y1 = 0
x2 = 4
y2 = 1
x3 = 0
y3 = 4

# x1 = int(input("valor de x1: "))
# y1 = int(input("valor de y1: "))
# x2 = int(input("valor de x2: "))
# y2 = int(input("valor de y2: "))
# x3 = int(input("valor de x3: "))
# y3 = int(input("valor de y3: "))
# d1 = int(input("distancia beacon 1: "))
# d2 = int(input("distancia beacon 2: "))
# d3 = int(input("distancia beacon 3: "))

n1 = 1.46
n2 = 1.59
n3 = 1.54
# 90
RSSdo1 = -49
# 4C
RSSdo2 = -50
# 3C
RSSdo3 = -53
# 90
RSSI1 = -50
# 4C
RSSI2 = -55
# 3C
RSSI3 = -57

# n1 = float(input("n1: "))
# RSSdo1 = int(input("RSSdo1: "))
# RSSI1 = int(input("RSSI1:"))
# n2 = float(input("n2: "))
# RSSdo2 = int(input("RSSdo2: "))
# RSSI2 = int(input("RSSI2:"))
# n3 = float(input("n3: "))
# RSSdo3 = int(input("RSSdo3: "))
# RSSI3 = int(input("RSSI3:"))

# calculo da distancia

d1 = np.round(np.power(10,((RSSdo1 - RSSI1)/(10*n1))),2)

d2 = np.round(np.power(10,((RSSdo2 - RSSI2)/(10*n2))),2)

d3 = np.round(np.power(10,((RSSdo3 - RSSI3)/(10*n3))),2)

print(d1)
print(d2)
print(d3)

# Trilateracao

A1 = 2*(x2-x1)
A2 = 2*(x3-x1)
A3 = 2*(x3-x2)


B1 = 2*(y2-y1)
B2 = 2*(y3-y1)
B3 = 2*(y3-y2)


C1 = d1 - d2 + np.power(x2,2) - np.power(x1,2) + np.power(y2,2) - np.power(y1,2)
C2 = d1 - d3 + np.power(x3,2) - np.power(x1,2) + np.power(y3,2) - np.power(y1,2)
C3 = d2 - d3 + np.power(x3,2) - np.power(x2,2) + np.power(y3,2) - np.power(y2,2)



Mtr0 = np.array([[np.power(A1,2)+np.power(A2,2)+np.power(A3,2), A1*B1+A2*B2+A3*B3],
                [A1*B1+A2*B2+A3*B3, np.power(B1,2)+np.power(B2,2)+np.power(B3,2)]])


Mtr1 = np.linalg.inv(Mtr0)

Mtr2 = np.array([[A1*C1+A2*C2+A3*C3],
                [B1*C1+B2*C2+B3*C3]])

coordenadas = np.round(np.dot(Mtr1,Mtr2),2)

print(coordenadas)

# # log distance
# distancia = np.power(10,((RSSd0 - RSSImedio)/10*n))
# # calculo do n
# RSSI = []
# nList = []
# for i in RSSI:
#     ene = (RSSd0 - RSSI[i])/(10*log10(d))
#     nList.append(ene)


