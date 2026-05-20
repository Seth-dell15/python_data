from math import log
import numpy as np
#This exercice will be about Logs
#Pour rappel : Le logarithme répond en fait à la question suivante : « À quelle puissance dois-je élever la base pour obtenir ce nombre ? »

arr = np.arange(1, 10)#Tableau de 1 à 9

print(np.log2(arr))#Log base 2

arr1 = np.arange(1, 10)

print(np.log10(arr1))#Log base 10

arr2 = np.arange(1, 10)

print(np.log(arr2))#Log base e / ln(x) -> e =approx 2,718

nplog = np.frompyfunc(log, 2, 1) # -> log = what we want to transform 2 = input(x and base) 1 = output

print(nplog(100, 15))#Log at any base