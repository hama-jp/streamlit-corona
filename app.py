import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 厚生労働省の公開データ
url = 'https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv'
df = pd.read_csv(url, parse_dates=[0])

st.sidebar.write('表示データを選択してください。')
days = st.sidebar.slider('## 表示日数選択（過去日）', 1, 365*2, 365)

st.title('一日あたりの陽性者数')
pref=st.multiselect(
    '表示データを選択してください。',
    list(df.columns[1:]),
    ['Tokushima', 'Kagawa', 'Ehime', 'Kochi']
)
fig = px.line(df[-days:], x='Date', y=pref, title="新型コロナ陽性者数の推移")
st.write(fig)
