import streamlit as st
import pandas as pd
import numpy as np

from pandas.core.generic import pickle
#from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor

header = st.container()
features = st.container()

with header:
    st.title("Delhi Flats Price!")
    st.text("In this project the price of Flats in Delhi are predicted...")
    
    
    
with features:
    st.header("Inputs")
    st.text("Please enter the relevant data for price prediction")
    sel_col, disp_col = st.columns([5,1])
    area_sel = sel_col.slider("area (sq ft)",min_value=810,max_value=2080,value=1302,step=1)
    latitude_sel = sel_col.slider("latitude",min_value=28.24,max_value=28.79,value=28.56,step=0.01)
    longitude_sel = sel_col.slider("longitude",min_value=76.88,max_value=77.56,value=77.29,step=0.01)
    Bedrooms_sel = sel_col.slider("Bedrooms",min_value=2,max_value=10,value=3,step=1)
    Balcony_sel = sel_col.slider("Balcony",min_value=1,max_value=10,value=2,step=1)

a = np.array([[0]]*5).reshape(1,5)
df_new = pd.DataFrame(a)
df_new.columns = ["area", "latitude", "longitude", "Bedrooms", "Balcony"]

df_new['area'] = area_sel
df_new['latitude'] = latitude_sel
df_new['longitude'] = longitude_sel
df_new['Bedrooms'] = Bedrooms_sel
df_new['Balcony'] = Balcony_sel

pkl_filename = "pickle_model_best.pkl"
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

#price
if st.button('Make Prediction'):
    estimate_price = pickle_model.predict(df_new.values)[0]
   
    
    seperator_of_thousand = "."
    seperator_of_fraction = ","
    estimate_price = "{:,.2f}".format(estimate_price)
    if seperator_of_thousand == ".":
        main_currency, fractional_currency = estimate_price.split(".")[0], estimate_price.split(".")[1]
        new_main_currency = main_currency.replace(",", ".")
        currency = new_main_currency + seperator_of_fraction + fractional_currency
        print(estimate_price)
    st.write(f"The estimated price is: Rs {estimate_price}")
