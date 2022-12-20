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
    area_sel = sel_col.slider("area",min_value=810,max_value=2080,value=1302,step=1)
    latitude_sel = sel_col.slider("latitude",min_value=28.24,max_value=28.79,value=28.56,step=0.01)
    longitude_sel = sel_col.slider("longitude",min_value=76.88,max_value=77.56,value=77.29,step=0.01)
    Bedrooms_sel = sel_col.slider("Bedrooms",min_value=2,max_value=10,value=3,step=1)
    Balcony_sel = sel_col.slider("Balcony",min_value=1,max_value=10,value=2,step=1)

a = np.array([[0]]*5).reshape(1,5)
df_new = pd.DataFrame(a)
df_new.columns = ["area", "latitude", "longitude", "Bedrooms", "Balcony"]


