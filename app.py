import streamlit as st
import pandas as pd
import numpy as np
from pandas.core.generic import pickle
from sklearn.ensemble import RandomForestRegressor

header = st.container()
features = st.container()

with header:
    st.title("Delhi Flats Price!")
    st.text("In this project the price of Flats in Delhi are predicted...")


     


