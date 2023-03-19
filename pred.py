import keras
import data
import model
import pandas as pd
import numpy as np


X = data.data_assembly()
pred = model.pred(X)

print(pred)