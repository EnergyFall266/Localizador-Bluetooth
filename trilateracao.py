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
y3 = 12





# x1 = int(input("valor de x1: "))
# y1 = int(input("valor de y1: "))
# x2 = int(input("valor de x2: "))
# y2 = int(input("valor de y2: "))
# x3 = int(input("valor de x3: "))
# y3 = int(input("valor de y3: "))
# d1 = int(input("distancia beacon 1: "))
# d2 = int(input("distancia beacon 2: "))
# d3 = int(input("distancia beacon 3: "))

# n1 = 2.48
# n2 = 2.80
# n3 = 1.88

# RSSdo1 = -47

# RSSdo2 = -47

# RSSdo3 = -48

# RSSI1 = -78

# RSSI2 = -65

# RSSI3 = -60

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

# d1 = np.round(np.power(10,((RSSdo1 - RSSI1)/(10*n1))),2)

# d2 = np.round(np.power(10,((RSSdo2 - RSSI2)/(10*n2))),2)

# d3 = np.round(np.power(10,((RSSdo3 - RSSI3)/(10*n3))),2)

# print(d1)
# print(d2)
# print(d3)

# Trilateracao

A1 = 2*(x2-x1)
A2 = 2*(x3-x1)
A3 = 2*(x3-x2)


B1 = 2*(y2-y1)
B2 = 2*(y3-y1)
B3 = 2*(y3-y2)



with open('datasetRNAtrilat1.csv','r') as f:
    reader = csv.reader(f)
    dist1 = list(reader)
with open('datasetRNAtrilat2.csv','r') as s:
    reader = csv.reader(s)
    dist2 = list(reader)
with open('datasetRNAtrilat3.csv','r') as b:
    reader = csv.reader(b)
    dist3 = list(reader)

flat_list1 = []
flat_list2 = []
flat_list3 = []
for xs in dist1:
    for x in xs:
        flat_list1.append(x)

for gs in dist2:
    for g in gs:
        flat_list2.append(g)

for hs in dist3:
    for h in hs:
        flat_list3.append(h)

d1 = list(map(float, flat_list1))

d2 = list(map(float, flat_list2))

d3 = list(map(float, flat_list3))

# # d1 = 7.16
# # d2 = 1.78
# # d3 = 9.52
i=0
while i<len(d1):

# C1 = np.power(d1,2) - np.power(d2,2) + np.power(x2,2) - np.power(x1,2) + np.power(y2,2) - np.power(y1,2)
# C2 = np.power(d1,2) - np.power(d3,2) + np.power(x3,2) - np.power(x1,2) + np.power(y3,2) - np.power(y1,2)
# C3 = np.power(d2,2) - np.power(d3,2) + np.power(x3,2) - np.power(x2,2) + np.power(y3,2) - np.power(y2,2)

    C1 = d1[i] - d2[i] + np.power(x2,2) - np.power(x1,2) + np.power(y2,2) - np.power(y1,2)
    C2 = d1[i] - d3[i] + np.power(x3,2) - np.power(x1,2) + np.power(y3,2) - np.power(y1,2)
    C3 = d2[i] - d3[i] + np.power(x3,2) - np.power(x2,2) + np.power(y3,2) - np.power(y2,2)

    # C1 = d1 - d2 + np.power(x2,2) - np.power(x1,2) + np.power(y2,2) - np.power(y1,2)
    # C2 = d1 - d3 + np.power(x3,2) - np.power(x1,2) + np.power(y3,2) - np.power(y1,2)
    # C3 = d2 - d3 + np.power(x3,2) - np.power(x2,2) + np.power(y3,2) - np.power(y2,2)

    Mtr0 = np.array([[np.power(A1,2)+np.power(A2,2)+np.power(A3,2), A1*B1+A2*B2+A3*B3],[A1*B1+A2*B2+A3*B3, np.power(B1,2)+np.power(B2,2)+np.power(B3,2)]])

    Mtr1 = np.linalg.inv(Mtr0)

    Mtr2 = np.array([[A1*C1+A2*C2+A3*C3],
                    [B1*C1+B2*C2+B3*C3]])

    coordenadas = np.round(np.dot(Mtr1,Mtr2),2)
# print(coordenadas)
    with open('trilatRNACoord.csv', 'a') as f:
                f.write(f'{coordenadas[0][0]},{coordenadas[1][0]}\n')
    i+=1


# # log distance
# distancia = np.power(10,((RSSd0 - RSSImedio)/10*n))
# # calculo do n
# RSSI = []
# nList = []
# for i in RSSI:
#     ene = (RSSd0 - RSSI[i])/(10*log10(d))
#     nList.append(ene)


