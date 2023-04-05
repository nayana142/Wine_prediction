import streamlit as st
import pandas as pd
from sklearn import datasets
st.title('Wine prediction')
st.write('''
Simple wine color  prediction app
''')

st.sidebar.header('User input parameters')
def user_input_features():
    fixed_acidity = st.sidebar.slider('fixed_acidity', 3.8, 15.9, 5.4)
    volatile_acidity = st.sidebar.slider('volatile_acidity', 0.08, 1.58, 1.4)
    citric_acid = st.sidebar.slider('citric_acid', 0.0, 1.66, 1.3)
    residual_sugar = st.sidebar.slider('residual_sugar', 0.6, 65.8, 1.2)
    chlorides = st.sidebar.slider('chlorides', 0.009, 0.611, 0.4)
    free_sulfur_dioxide = st.sidebar.slider('free_sulphur_dioxide', 1.0, 289.0, 38.0)
    total_sulfur_dioxide = st.sidebar.slider('total_sulphur_dioxide', 6.0, 440.0, 10.0)
    density = st.sidebar.slider('density', 0.99, 1.04, 1.0)
    pH = st.sidebar.slider('pH', 2.72, 4.01, 3.4)
    sulphates = st.sidebar.slider('sulphates', 0.22, 2.0, 1.3)
    alcohol = st.sidebar.slider('alcohol', 8.0, 14.9, 5.0)
    quality = st.sidebar.slider('quality', 3.0, 9.0, 5.0)

    data = {'fixed_acidity': fixed_acidity,
            'volatile_acidity': volatile_acidity,
            'citric_acid': citric_acid,
            'residual_sugar': residual_sugar,
            'chlorides': chlorides,
            'free_sulfur_dioxide': free_sulfur_dioxide,
            'total_sulfur_dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol,
            'quality': quality
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

wine = pd.read_csv('Wine_Quality_Data.csv')
wine.color=wine.color.map({"red":1,"white":0})
x = wine.drop('color',axis=1)
y = wine.color

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x1=scaler.fit_transform(x)
x1=pd.DataFrame(x1,columns=x.columns)

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
logsk = LogisticRegression()
logsk.fit(x1,y)

## prediction
prediction =logsk.predict(df)
prediction_proba=logsk.predict_proba(df)

if prediction==1:
    prediction='red'
if prediction==0:
    prediction='white'


st.subheader('prediction')
st.write(prediction)

st.subheader('prediction probability')
st.write(prediction_proba)