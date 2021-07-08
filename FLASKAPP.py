from flask import Flask, render_template
from flask import request
from flask import redirect, url_for
import os
import pickle
import numpy as np
import pandas as pd
import scipy
import sklearn
import skimage
import skimage.color
import skimage.transform
import skimage.feature
import skimage.io
from sklearn.preprocessing import StandardScaler
from enum import Enum

app=Flask(__name__)
pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

class Species(Enum):
 Bream = 0
 Roach = 1
 Whitefish = 2
 Parkki = 3
 Perch = 4
 Pike = 5
 Smelt = 6

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = list(map(float, [x for x in request.form.values()]))
    
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    predict = Species(prediction[0])
    print(Species(prediction[0]))
    return render_template('index.html', prediction_text='The fish belong to {} '. format(Species(prediction[0])))

if __name__=='__main__':
    app.run()