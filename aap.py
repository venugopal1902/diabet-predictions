from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

import pickle
import numpy as np
model = pickle.load(open('venu.pkl', 'rb'))
app = Flask(__name__)


def predict():
    Age = input('Enter your Age',type=NUMBER)
    BMI = input('Enter your Bobymass Index',type=FLOAT)
    Glucose =  input('Enter your Glucoselevel',type=NUMBER)
    BloodPressure = input('Enter your Blood Pressure',type=NUMBER)
    Pregnancies = input('Enter no.of Pregnancies(if your are a man enter 0)',type=NUMBER)
    SkinThickness = input('Enter your Skin Thickness',type=NUMBER)
    DiabetesPedigreeFunction = input('Enter your DiabetesPedigreeFunction',type=FLOAT)
    Insulin = input('Enter your Insulin',type=NUMBER)                                 
    

    output = model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    

    if output == 1 :
        put_text("Diabetes : Positive")
    
    else: 
        put_text('Diabetes : Negative')
        

app.add_url_rule('/', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)

