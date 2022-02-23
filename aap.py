from select import select
from flask import Flask
from pywebio.input import *
from pywebio.output import *
from pywebio.output import put_text 
from pywebio import start_server
import pandas as pd
import pickle
import numpy as np
model = pickle.load(open('venu.pkl', 'rb'))
app = Flask(__name__)


def predict():
    
    Age = input('Enter your Age',type=NUMBER,name=f's{2}')
    BMI = input('Enter your Bobymass Index',type=FLOAT,name=f's{3}')
    Glucose =  input('Enter your Glucoselevel',type=NUMBER,name=f's{4}')
    BloodPressure = input('Enter your Blood Pressure',type=NUMBER,name=f's{5}')
    Pregnancies = input('Enter no.of Pregnancies(if your are a man enter 0)',type=NUMBER,name=f's{6}')
    SkinThickness = input('Enter your Skin Thickness',type=NUMBER,name=f's{8}')
    DiabetesPedigreeFunction = input('Enter your DiabetesPedigreeFunction',type=FLOAT,name=f's{9}')
    Insulin = input('Enter your Insulin',type=NUMBER,name=f's{10}')    
                                 
    d = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
    d = input_group('basic info',d)
    d= list(d.values())

    output = model.predict([d])
    

    if output == 1 :
        put_html("<h2>Diabetes : Positive</h2>")
    
    else: 
        put_html('<h2>Diabetes : Negative</h2>')
    put_html('<a href="/" style="background-color:blue;margin-left:350px;color:white;;padding :8px;border-radius:5px;font-size:30px;text-decoration:none;box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)">Home</a>') 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)
# if __name__ == '__main__':
#        start_server(predict, port=8000, debug=True)

app.add_url_rule('/', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)

