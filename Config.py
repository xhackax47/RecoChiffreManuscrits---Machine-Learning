from sklearn import datasets
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np
import time

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 13:35:30 2023

@author: samy_
"""
# Variables

digits = datasets.load_digits()
digitsTarget = digits.target
mlp = MLPClassifier(hidden_layer_sizes=(15,))
digitsTab1D = digits.images.reshape((len(digits.images), -1))
digitsTab1D_train = digitsTab1D[:1000]
digitsTarget_train = digitsTarget[:1000]
digitsTab1D_test = digitsTab1D[1000:]
digitsTarget_test = digitsTarget[1000:]

# Fonctions

def programme():
    print("INITIALISATION ET DEMARRAGE DU PROGRAMME DE RECONNAISSANCE DE CHIFFRES MANSUSCRITS")
    time.sleep(5)
    afficherDigitsImage()
    afficherGraphImage()
    afficherDigitsImage()
    entrainement1000img(digitsTab1D_train, digitsTarget_train, mlp)
    evalPerf(digitsTab1D_test, digitsTarget_test, mlp)
    print("FIN DU PROGRAMME")

def afficherDigitsImage():
    print("Affichage de l'image")
    print(digits.images[0])
    time.sleep(2)
    
def afficherGraphImage():
    print("Affichage de l'image via Plt")
    plt.imshow(digits.images[0],cmap='binary')
    plt.title(digits.target[0])
    plt.axis('off')
    plt.show()
    time.sleep(2)
    
def entrainement1000img(digitsTab1D_train, digitsTarget_train, classifier):
    print("Début de l'entraînement du modèle sur 1000 itérations")
    classifier.fit(digitsTab1D_train, digitsTarget_train)
    print("Fin de l'entraînement du modèle sur 1000 itérations")
    time.sleep(2)
    
def evalPerf(digitsTab1D_test, digitsTarget_test, classifier):
    print("Test de prédictions et validation des résultats par comparaison et calcul du taux d'erreur")
    digitsTarget_pred = mlp.predict(digitsTab1D_test)
    error = (digitsTarget_pred != digitsTarget_test)
    tauxErreur = np.sum(error) / len(digitsTarget_test)
    print("Le taux d'erreur de ce modèle est d'environ : " + str(tauxErreur))
    time.sleep(2)
    digitsTab1D_error = digitsTab1D_test[error].reshape((-1, 8,8))
    digitsTarget_error = digitsTarget_test[error]
    digitsTarget_pred_error = digitsTarget_pred[error]
    print("Affichage des erreurs de prédictions.")
    i = 10
    plt.imshow(digitsTab1D_error[i],cmap='binary')
    plt.title(f'cible: {digitsTarget_error[i]}, prediction: {digitsTarget_pred_error[i]}')
    plt.axis('off')
    plt.show()
    time.sleep(2)
