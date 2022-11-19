import pickle
from tabpy.tabpy_tools.client import Client
import pandas as pd
import numpy as np
model=pickle.load(open('dtmodel.sav','rb'))

tabpy

def predict_student(model,X_test):
    model=pickle.load(open('dtmodel.sav','rb'))
    y_pred=model.predict(X_test)
    return y_pred

 

conn=Client('http://localhost:9004/')

conn.set_credentials('nmurugesh','N_Murugesh123')

conn.deploy('predict_student',
predict_student, 'Returns prediction of student conversion'
, override = True)