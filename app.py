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
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myapplication")

try:
    with st.form(key='my_form'):
        st.header('Price Pridiction')
        a = st.number_input('Enter the area in sq .ft',1000,6000, key=1)
        b = st.number_input('Enter number of Rooms',1,20, key=2)
        loc = st.text_input('Enter Location(Eg. Juhu)', key=3)
        e = st.checkbox('24X7Security', key=4)
        f = st.checkbox('Rain Water Harvesting', key=5)
        g = st.checkbox('Childrens Playground', key=6)
        i = st.checkbox('Power Backup', key=7)
       
        submit_button = st.form_submit_button(label='Submit')
        location = geolocator.geocode(loc)
        c = location.latitude
        d = location.longitude
        ar = arr.array('f',[a,b,c,d,e,f,g,i])
        data = pd.read_csv("Final.csv")
        data.drop(data.columns[2],axis= 1, inplace = True)
        #data.drop([data.columns[i] for i in range(3,14)],axis= 1, inplace = True)
      
        model  = KNeighborsRegressor()
        features = data[['Area','No. of Bedrooms','Latitude','Longitude','24X7Security','RainWaterHarvesting','Childrensplayarea','PowerBackup']]
        label = data["Price"]
        model.fit(features.values, label.values)
        pred = model.predict([ar])
        #pred = model.predict([[100,1,65.3456,29.4535]])
        print(pred)
        st.text('Estimate Rs.')
        st.text(pred[0])

except AttributeError:
      pass