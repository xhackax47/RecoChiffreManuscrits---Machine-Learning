from sklearn import datasets
import matplotlib.pyplot as plt

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 13:25:43 2023

@author: samy_
"""

digits = datasets.load_digits()
print(digits.images[0])