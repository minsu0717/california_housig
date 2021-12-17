import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

from eda_app import run_eda_app

def main():
    st.title('미국 집값 예측하기')
    
    menu = ['Home','EDA','ML']
    choice=st.sidebar.selectbox('메뉴',menu)
    
    if choice == 'Home':
        st.text('미국 집 값을 예측합니다. 조건을 입력하시면 예측이 됩니다')
        st.text('옆에 메뉴를 눌러주세요')
        
        st.image('http://image.chosun.com/sitedata/image/201810/29/2018102902845_0.jpg')
    
    elif choice == 'EDA':
        run_eda_app()
    
    elif choice == 'ML':
        pass

if __name__ == '__main__':
    main()