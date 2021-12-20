import streamlit as st
import pandas as pd
import numpy as np
import joblib

def run_ml_app():
    st.subheader('Machine Learning 예측')
    
    bedrooms=st.number_input('bedrooms 입력',min_value=1,max_value=9)
    bathrooms=st.number_input('bathrooms 입력',min_value=1,max_value=8)
    sqft_living=st.number_input('sqft_living 입력',min_value=370,max_value=13540)
    sqft_lot=st.number_input('sqft_lot 입력',min_value=638,max_value=1100000)
    floors=st.number_input('floors입력',min_value=1,max_value=4)
    waterfront=st.number_input('waterfront 입력',min_value=0,max_value=1)
    view=st.number_input('view 입력',min_value=0,max_value=4)
    condition=st.number_input('condition 입력',min_value=1,max_value=5)
    sqft_above=st.number_input('sqft_above 입력',min_value=370,max_value=9410)
    sqft_basement=st.number_input('sqft_basement 입력',min_value=1,max_value=4820)
    year_built=st.number_input('year_built 입력',min_value=1900,max_value=2014)
    