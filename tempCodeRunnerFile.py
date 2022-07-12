from cmath import log10
from turtle import distance
import numpy as np
from sympy import Matrix
import csv

x1 = 7
y1 = 0
x2 = 11
y2 = 8
x3 = 0
y3 = 11





# x1 = int(input("valor de x1: "))
# y1 = int(input("valor de y1: "))
# x2 = int(input("valor de x2: "))
# y2 = int(input("valor de y2: "))
# x3 = int(input("valor de x3: "))
# y3 = int(input("valor de y3: "))
# d1 = int(input("distancia beacon 1: "))
# d2 = int(input("distancia beacon 2: "))
# d3 = int(input("distancia beacon 3: "))

n1 = 2.48
n2 = 2.80
n3 = 1.88

RSSdo1 = -47

RSSdo2 = -47

RSSdo3 = -48

RSSI1 = -76

RSSI2 = -48

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
