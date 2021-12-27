import streamlit as st
import pandas as pd
import numpy as np
import joblib

def run_ml_app():
    st.subheader('Machine Learning 예측')
    st.text('코랩에서 코딩을 하였고,MinMaxScaler를 사용했습니다.')
    df=pd.read_csv('data/housing.csv')
    df=df.dropna()
    df=df.iloc[:1000,:]
    
    st.image('https://www.researchgate.net/profile/Maria-Fonseca-47/publication/325722746/figure/fig4/AS:636796719345665@1528835577892/Figura-1-Condados-counties-do-Estado-da-California-mapa-de-referencia.png')
    st.write('위의 사진을 보고 위도와 경도를 설정해주세요')
    longitude=st.slider('경도 ',min_value=df['longitude'].min(),max_value=df['longitude'].max())
    latitude=st.slider('위도 ',min_value=df['latitude'].min(),max_value=df['latitude'].max())
    housing_median_age=st.number_input('집 지어진 기간 ',min_value=df['housing_median_age'].min(),max_value=df['housing_median_age'].max())
    total_rooms=st.slider('블록 내 총 방수 ',min_value=df['total_rooms'].min(),max_value=df['total_rooms'].max())
    total_bedrooms=st.slider('한 블록 내 침실 수 ',min_value=df['total_bedrooms'].min(),max_value=df['total_bedrooms'].max())
    population=st.number_input('인구 수 ',min_value=df['population'].min(),max_value=df['population'].max())
    households=st.number_input('세대 수 ',min_value=df['households'].min(),max_value=df['households'].max())
    median_income=st.number_input('중간 소득 ',min_value=df['median_income'].min(),max_value=df['median_income'].max())
    
    
    
    new_data = np.array([longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income])
    new_data = new_data.reshape(1,8)
    
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')
    regressor = joblib.load('data/regressor.pkl')
    
    new_data = scaler_X.transform(new_data)
    y_pred=regressor.predict(new_data)
    y_pred=scaler_y.inverse_transform(y_pred.reshape(1,1))
    
    if st.button('예측 결과 보기'):
        st.write('예측 결과! 중간 주택 가격 {}달러를 살 수 있습니다.'.format(round(y_pred[0][0]),2))
    
    