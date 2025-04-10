'''import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit 제목
st.title('항공기 사고 데이터 분석 대시보드')

# 데이터 불러오기
data = pd.read_csv('aircraft-data_nov_dec.csv')

# 컬럼명 확인
st.write('컬럼 목록:', list(data.columns))

st.write('데이터 미리보기:')
st.write(data.head())

# 사고 연도별 발생 건수 시각화
data['Year'] = pd.to_datetime(data['reg_expiration'], errors='coerce').dt.year
yearly_counts = data['Year'].value_counts().sort_index()

st.write('연도별 사고 건수:')
fig, ax = plt.subplots()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Accidents')
ax.set_title('Yearly Aircraft Accidents')
st.pyplot(fig)

# 주(State)별 사고 건수
st.write('주(State)별 사고 건수:')
state_counts = data['reg_state'].dropna().value_counts().head(10)

fig2, ax2 = plt.subplots()
sns.barplot(x=state_counts.values, y=state_counts.index, ax=ax2)
ax2.set_xlabel('Number of Accidents')
ax2.set_ylabel('State')
ax2.set_title('Top 10 States by Aircraft Accidents')
st.pyplot(fig2)
'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 제목
st.title('항공기 이상 탐지 대시보드')

# 데이터 불러오기
data = pd.read_csv('aircraft-data_nov_dec.csv')

# 컬럼 확인 (디버깅용)
# st.write(data.columns)

# 데이터 전처리
data['reg_expiration'] = pd.to_datetime(data['reg_expiration'], errors='coerce')

# 이상 탐지 로직
altitude_anomalies = data[(data['alt'] > 50000) | (data['alt'] < 1000)]
speed_anomalies = data[data['mph'] > 600]
expired_registration = data[data['reg_expiration'] < pd.Timestamp.today()]

# 대시보드
st.header('📊 데이터 개요')
st.write(data.head())

st.header('📌 이상 탐지 결과')

st.subheader('1️⃣ 고도 이상 항공기 (1000ft 미만 또는 50000ft 초과)')
st.write(altitude_anomalies)

st.subheader('2️⃣ 속도 이상 항공기 (600 mph 초과)')
st.write(speed_anomalies)

st.subheader('3️⃣ 등록 만료된 항공기')
st.write(expired_registration)

# 추가 시각화
st.header('📈 항공기 데이터 시각화')

# 고도 분포
st.subheader('고도 분포')
fig, ax = plt.subplots()
sns.histplot(data['alt'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# 속도 분포
st.subheader('속도 분포')
fig, ax = plt.subplots()
sns.histplot(data['mph'], bins=30, kde=True, ax=ax)
st.pyplot(fig)

# 제조사 별 항공기 수
st.subheader('제조사 별 항공기 수')
fig, ax = plt.subplots()
data['manufacturer'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

st.success('✅ 대시보드가 성공적으로 로드되었습니다!')
