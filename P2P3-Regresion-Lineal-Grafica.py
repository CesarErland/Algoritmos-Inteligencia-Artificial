# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:11:31 2023

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
r=np.random.normal(0,1,size=x.shape)
y_s=3*x+5
y=y_s+r
alfa=0.02
w=1
n_epochs=10
error=[]
for n in range(n_epochs):
    y_e=w*x
    e=np.sum(np.power((y_e-y),2))/200
    error.append(e)
    w=w-alfa*(np.sum((y_e-y))*x)/100
    print(w)
i=np.arange(0,n_epochs)
plt.scatter(i, error)

plt.scatter(x, y,marker='*')