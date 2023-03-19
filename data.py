import pandas as pd
import numpy as np

x = {'exang': [1, 1, 0, 1], 'cp': [2, 0, 2, 0], 'thalach': [163, 125, 152, 95], 'oldpeak': [0.0, 0.9, 0.0, 2.0], 'slope': [2, 1, 1, 1], 'ca': [1, 2, 0, 2], 'thal': [2, 2, 2, 3]}


def data_collect(a):
    a1 = a.split(', ')
    global x
    x['exang'].append(int(a1[0]))
    x['cp'].append(int(a1[1]))
    x['thalach'].append(int(a1[2]))
    x['oldpeak'].append(float(a1[3]))
    x['slope'].append(int(a1[4]))
    x['ca'].append(int(a1[5]))
    x['thal'].append(int(a1[6]))
    return(x)


def data_assembly(x):
    X = pd.DataFrame(np.c_[x['exang'], x['cp'], x['thalach'], x['oldpeak'], x['slope'], x['ca'], x['thal']], columns=['exang', 'cp', 'thalach', 'oldpeak', 'slope', 'ca', 'thal'])
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    X -= mean
    X /= std
    X -= mean
    X /= std
    return(X)
