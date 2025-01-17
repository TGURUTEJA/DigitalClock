
from flask import  Flask,render_template,request
import pandas as pd
import pickle

import numpy as np
app=Flask(__name__)
data=pd.read_csv('')


pipe=pickle.load(open('RidgModel.pkl','rb'))
@app.route('/')
def index():
    locations=sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict',methods=['Post'])
def predict():
    location=request.form.get('location')
    bhk=request.form.get('bhk')
    bath=request.form.get('bath')
    sqft=request.form.get('total_sqrt')
    input=pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction=pipe.predict(input)[0]*1e5
    st=str(np.round(prediction))
    return st

if __name__=="__main__":
    app.run(debug=True,port=5001)