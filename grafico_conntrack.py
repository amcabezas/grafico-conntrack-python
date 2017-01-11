# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from dateutil.parser import parse
conntrack = open('conntrack.txt', 'r') #archivo conntrack
date = open('date.txt', 'r')# archivo data
con = []
fechas = []
for linea in open('conntrack.txt', 'r'):
    con.append(linea)


for fecha in date.readlines(): # formato Sat Oct  8 20:00:01 CLST 20167
    date = parse(fecha) # cambio de formato 2016-10-08 20:00:01-03:00
    fechas.append(date)

plt.title(u"Conntrack Status")# Titulo
plt.plot(fechas,con) # ejes (x,y)
plt.xlabel('From Oct 8 2016 to Jan 10 2017')  # Colocamos la etiqueta en el eje x
plt.ylabel('Connections')  # Colocamos la etiqueta en el eje y
plt.show()
