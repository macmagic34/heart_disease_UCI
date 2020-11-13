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

model = pickle.load(open('LRModel.pkl', 'rb'))
df = pd.read_csv('heart.csv')
ss = StandardScaler()
ss.fit(df[['ca', 'cp', 'exang', 'oldpeak', 'thal']])



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

        sex_dict = {'Male':1, 'Female':0} 
        angina_dict = {'Yes':1, 'No':0}
# =============================================================================
        features = [vessel, cp, angina_dict[angina], oldpeak,  csr.split()[0]]
        ss.transform(features)
#        val = model.predict(features)
# =============================================================================
    except:
# =============================================================================
        return '''<h2>One or more values were not selected before predicting, please try again..</h2>
                    values collected: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
                    '''.format(cp, angina_dict[angina], oldpeak, vessel, csr.split()[0])
# =============================================================================

    return "hi"







    
app.run(debug=True)