from statistics import LinearRegression

import requests
from requests.api import head
import csv
import array as arr
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import string
from sklearn.preprocessing import OrdinalEncoder
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myapplication")

try:
    with st.form(key='my_form'):
        st.header('Price Pridiction')
        a = st.number_input('Enter the area in sq .ft', key=1)
        b = st.number_input('Enter number of Rooms', key=2)
        loc = st.text_input('Enter Location(Eg. Juhu)', key=3)
        submit_button = st.form_submit_button(label='Submit')
        location = geolocator.geocode(loc)
        c = location.latitude
        d = location.longitude
        ar = arr.array('f',[a,b,c,d])
        data = pd.read_csv("Final.csv")
        data.drop(data.columns[2],axis= 1, inplace = True)
        data.drop([data.columns[i] for i in range(3,39)],axis= 1, inplace = True)
        model  = KNeighborsClassifier()
        features = data[['Area','No. of Bedrooms','Latitude','Longitude']]
        label = data["Price"]
        model.fit(features.values, label.values)
        pred = model.predict([ar])
        #pred = model.predict([[100,1,65.3456,29.4535]])
        print(pred)
        st.text('Estimate Rs.')
        st.text(pred[0])

except AttributeError:
      pass

   
