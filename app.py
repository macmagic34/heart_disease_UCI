# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 15:44:19 2020

@author: TR3X
"""

from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

model = pickle.load(open('RFModel_5_in.pkl', 'rb'))
df = pd.read_csv('heart.csv')



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        cp = request.form['chest']
        angina = request.form['Angina']
        oldpeak = request.form['Oldpeak']
        vessel = request.form['vessels']
        csr = request.form['CSR']
        sex = request.form['sex']
        sex_dict = {'Male':1, 'Female':0} 
        angina_dict = {'Yes':1, 'No':0}
# =============================================================================
        features = [np.array([int(vessel), int(cp), int(angina_dict[angina]), int(oldpeak),  sex_dict[sex]])]
        val = model.predict(features)
        if val[0]==0:
            text = 'Your heart is healthy'
        else:
            text = 'Your heart is unhealthy'
# =============================================================================
    except:
# =============================================================================
        return '''<h2>One or more values were not selected before predicting, please try again..</h2>
                    '''
# =============================================================================

    return render_template('index.html', prediction= text)







if __name__ == '__main__':
    app.run(debug=True)