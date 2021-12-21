import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    st.title('1990년도 캘리포니아 집값 분석')
    
    menu = ['Home','EDA','ML']
    choice=st.sidebar.selectbox('메뉴',menu)
    
    if choice == 'Home':
        st.text('1990년도 특정 캘리포니아 지역에서 발견된 주택과 관련되어서')
        st.text('1990년도 데이터를 기반으로 한 자료입니다.')
        
        st.text('옆에 메뉴를 눌러주세요')
        
        st.image('https://www.visitcalifornia.com/sites/visitcalifornia.com/files/styles/welcome_image/public/vc_perfectbeachtowns_lagunabeach_st_rf_637081844_1280x640_0.jpg')
    
    elif choice == 'EDA':
        run_eda_app()
    
    elif choice == 'ML':
        pass

if __name__ == '__main__':
    main()