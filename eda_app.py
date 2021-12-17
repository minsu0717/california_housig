import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app():
    
    st.subheader('EDA 화면 입니다.')
    
    df = pd.read_csv('data/data.csv')
    st.dataframe(df)
    if st.button('통계치'):
        st.write(df.describe())
        
    selected_cols=st.multiselect('보고싶은 컬럼을 선택하세요',df.iloc[:,1:].columns)
    if len(selected_cols) > 0 :
        st.write(df[selected_cols])
    else :
        st.write('선택된 컬럼이 없습니다')
        
    st.subheader('선택한 컬럼들의 상관관계 분석')
    st.text('데이터 전체의 히트맵')
    fig1=plt.figure(figsize=(10,5))
    sns.heatmap(df.corr(),annot=True,fmt='.1f',cmap='RdPu')
    plt.title('data correlation')
    st.pyplot(fig1)
    st.write(df.corr())
    
    selected_cols_corr=st.multiselect('컬럼들을 선택해주세요.',df.drop(columns=['date','street','city','statezip','country'],axis=1).columns)
    if len(selected_cols_corr) != 0 :
        st.write(df[selected_cols_corr].corr())
        fig2=sns.pairplot(data=df[selected_cols_corr],kind='reg')
        st.pyplot(fig2)
    else :
        st.write('선택한 컬럼이 없습니다.')
        
    st.subheader('집값이 가장 높은 곳과 가장 낮은 곳')
    df_ch=df.loc[df['price'] != 0,]
    radio_menu = ['높은곳','낮은곳']
    choice_radio=st.radio('선택하세요',radio_menu)
    if choice_radio == '높은곳':
        st.dataframe(df_ch.loc[df_ch['price'].max()==df_ch['price'],])
    else :
        st.dataframe(df_ch.loc[df_ch['price'].min()==df_ch['price'],])
        
    