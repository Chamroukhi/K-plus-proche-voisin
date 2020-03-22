#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:24:48 2020

@author: chamroukhi
"""

import numpy as np
import matplotlib.pyplot as plt

#base de données
x=[[12,23],[3,45],[56,67],[30,55],[78,69],[78,60],[14,50],[65,40],[80,50],[50,50]]
y=['+','+','-','+','-','-','+','-','-','-']

#nouvelle observation
a=[5,50]

#nombre de voisin k
k=4

#distance 
distancea=[]
distance=[]

#voisin 
voisin=[]

#classe de k voisin selectionner
classe_voisin=[]

#classe le plus apparait dans la liste classe voisin
majoritaire=[]

#distance euclidienne
def distanceE(o,x):
    """distance euclidienne"""
    s=0
    for i in range(2):
        s=s+(pow((o[i]-x[i]),2))
        d=np.sqrt(s)
        return d


#calculer la distance entre l'observation (0) et tout les point (Xi)       
for i in range(len(x)):
    d=distanceE(a, x[i])
    #stocker tous les distances dans les listes: distance et distancea
    distance.append(d)
    #distancea je crée cette liste car la liste distance a chaque 
    #valeur de i je elimine la distance minimale choisit.
    #mais je besoins de tous les distance pour selectionner le valeur de x[j]
    distancea.append(d)


#ici je choisit les K voisin grace a la distance euclidienne
for d in range(k) :
    #distance minimale 
    m=min(distance)
    
    for j in range(len(x)):
        
       #selectionner le point x et le classe y correspondant a la distance minimale
       if m == distancea[j]:
            if x[j] not in voisin:
                
                voisin.append(x[j])
                classe_voisin.append(y[j])
    #eliminer la distance minimale de la liste distance            
    distance.remove(m)

#calculer le nombre d'occurence de chaque classe_voisin
for i in range(len(classe_voisin)):
    
        maj=classe_voisin.count(classe_voisin[i])
        majoritaire.append(maj)

#selectionner le classe le plus apparait 
C=max(majoritaire)

#afficher la classe de l'observation
for c in range(len(classe_voisin)):
    if majoritaire[c]==C:
        classe_dobservation = classe_voisin[c]



X1=[]
X2=[]
for i in range(len(x)):
 
  X1.append(x[i][0])

  X2.append(x[i][1])


#présenter les nuages de point x,y
plt.scatter(X1,X2)

#tracer la droite y= a*x + b 
plt.show()

print("pour x =",a,"y=",classe_dobservation)        

