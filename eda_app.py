import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app():
    st.subheader('EDA 화면 입니다.\
        ec2 프리티어를 사용해서 느립니다. 양해 부탁 드립니다.')
    
    
    df=pd.read_csv('data/housing.csv')
    df.dropna(inplace=True)
    menu = ['컬럼 정보','데이터 프레임']
    sel_menu = st.radio('선택하세요',menu)
    if sel_menu == '컬럼 정보':
        st.text('longitude = 경도')
        st.text('latitude = 위도')
        st.text('housing_median_age = 주택 지어진 기간')
        st.text('total_rooms = 블록 내 총 방수')
        st.text('total_bedrooms = 한 블록 내 침실 수')
        st.text('population = 인구수')
        st.text('households = 세대수')
        st.text('median_income = 중간 소득')
        st.text('median_house_value = 중간 주택 가격')
        st.text('ocean_proximity = 바다 근접도')
    else :
        st.dataframe(df)
        st.text('통계치')
        st.write(df.describe())

    st.subheader('전체 데이터 시각화')
    st.map(df)
    df.hist(figsize=(10,10),bins=10)
    st.set_option('deprecation.showPyplotGlobalUse',False)
    st.pyplot()
    
    st.subheader('원하는 컬럼 보기')
    sel_col = st.multiselect('보고 싶은 컬럼을 선택 해주세요',df.columns)
    if len(sel_col) != 0:
        st.write(df[sel_col])
    else :
        st.write('선택한 컬럼이 없습니다')
        
    st.subheader('인구수가 가장 많은 곳과 적은 곳')
    radio_menu = ['많은 곳','적은 곳']
    choice_radio=st.radio('선택하세요',radio_menu)
    if choice_radio == '많은곳':
        st.map(df.loc[df['population'].max() == df['population'],])
        st.dataframe(df.loc[df['population'].max() == df['population'],])
    else :
        st.map(df.loc[df['population'].min() == df['population'],])
        st.dataframe(df.loc[df['population'].min() == df['population'],])
        
    st.subheader('세대 수가 가장 높은 곳과 낮은 곳')
    radio_menu_2 = ['높은 곳','낮은 곳']
    choice_radio_2 = st.radio('선택하세요',radio_menu_2)
    if choice_radio_2 == '높은 곳':
        st.map(df.loc[df['households'].max() == df['households'],])
        st.dataframe(df.loc[df['households'].max() == df['households'],])
    else :
        st.map(df.loc[df['households'].min() == df['households'],])
        st.dataframe(df.loc[df['households'].min() == df['households'],])
    
       
    st.subheader('가격에 따른 주택 데이터 표시')
    number = st.slider('선택',value=[df['median_house_value'].min(),df['median_house_value'].max()],min_value=df['median_house_value'].min(),max_value=df['median_house_value'].max())
    st.write(df.loc[(df['median_house_value']>=number[0])&(df['median_house_value']<=number[1]),])
    st.map(df.loc[(df['median_house_value']>=number[0])&(df['median_house_value']<=number[1]),])
        
    st.subheader('데이터 시각화')
    menu1=['위도와 경도에 따른 분포','건축 년도에 따른 주택 가격 평균','바다 근접도에 따른 가격 평균','상관관계 분석']
    sel_chart=st.selectbox('선택',menu1)
    if sel_chart == '위도와 경도에 따른 분포':
        df.plot(x='longitude',y='latitude',kind='scatter')
        plt.title('Distribution by latitude and longitude')
        st.pyplot()
    elif sel_chart == '건축 년도에 따른 주택 가격 평균':
        period = df.groupby('housing_median_age')['median_house_value'].mean()
        period.sort_values(inplace = True)
        index = period.index
        fig1 = plt.figure()
        plt.bar(index,period)
        plt.title('Housing_median_age Average Price')
        plt.xlabel('Housing_median_age')
        plt.ylabel('Average Price')
        st.pyplot(fig1)
        st.write(period)
    elif sel_chart == '바다 근접도에 따른 가격 평균':
        price = df.groupby('ocean_proximity')['median_house_value'].mean()
        price.sort_values(inplace=True)
        lable=price.index
        fig2 = plt.figure()
        plt.bar(lable,price)
        plt.title('Ocean_proximity Average Price')
        plt.ylabel('Average Price')
        st.pyplot(fig2)
        st.write(price)
    elif sel_chart == '상관관계 분석':
        fig3=plt.figure(figsize=(10,8))
        sns.heatmap(df.drop(columns=['longitude','latitude'],axis=1).corr(), annot=True, cmap='RdPu')
        plt.title('data correlation')
        st.pyplot(fig3)
        st.write(df.drop(columns=['longitude','latitude'],axis=1).corr())
        
    
        
    
  
        
    