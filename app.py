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
    
     balconies_sel = sel_col.slider("Balcony",min_value=1,max_value=10,value=0,step=1)

     


