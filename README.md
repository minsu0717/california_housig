# 캘리포니아 집값 분석

기획 : 1990년도 캘리포니아 집값에 대한 각각의 데이터를 시각화하였고, 집값 예측도 가능
설계: 파이썬 라이브러리의 Streamlit 기반의 프레임 워크 개발, 인공지능 사용 , Ec2로 배포


개발:  https://www.kaggle.com/datasets/camnugent/california-housing-prices 의 데이터 셋을 이용하였습니다.

데이터 프레임에 nan값이 있을 때 dropna()를 사용하여 nan 값 제거 

데이터프레임 컬럼에 대한 시각화를 위해 Streamlit library를 찾아보다가 st.map()을 이용하여 시각화 하는데 사용하였습니다 
그리고 상관관계 분석을 하기 위해 seaborn의 heatmap을 사용하였고, 각 컬럼의 분포의 상태를 시각화 하기 위해 데이터프레임의 .hist()와 plot의 scatter를 사용하여 히스토그램을 사용하였습니다.

주택 값 예측(수치 예측)을 위해 먼저 X와 y로 데이터를 분리 한 후, X와 y를 MinMaxScaler를 통해 데이터를 스케일링하고,
sklearn.model_selection에 train_test_split을 이용하여 트레이닝 셋과 테스트 셋을 나눈 다음 인공 지능은 sklearn에 RandomForestRegressor()를 사용 하였습니다 

테스트

Test 

ec2 배포
ec2 프리티어를 사용해서 많이 느리다



에러

인공지능을 사용하는데 어려움을 겪었다.

깃허브에 push 할 때 인공지능 파일이 커서 안올라갔다.


해결 

MinMaxSclaer를 할 때 X와 y 따로 스케일러 생성 , y는 판다스 시리즈 이기 때문에 reshape을 해줘야 한다.

파일질라 사용?



# 홈화면
![1](https://user-images.githubusercontent.com/96038772/161668858-f847bcba-3e39-492d-8861-8758a663d479.png)

# EDA화면
![2](https://user-images.githubusercontent.com/96038772/161668888-014d3354-6cc8-4081-817c-df9bf42c71d6.png)
![3](https://user-images.githubusercontent.com/96038772/161668903-18102b82-53db-42f0-9e59-c3611eb393a7.png)
![6](https://user-images.githubusercontent.com/96038772/161668959-a793f853-59d8-4940-b2fe-8493064ab0f0.png)
![7](https://user-images.githubusercontent.com/96038772/161668965-266f5854-07ca-4537-aa45-1dca9c85deaf.png)
![8](https://user-images.githubusercontent.com/96038772/161668970-5dc80c51-1dab-47ae-87a9-a3ac3c31b1ca.png)

# ML

