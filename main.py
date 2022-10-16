import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')
"gitに挑戦！！2022年10月15日"
"失敗したので再度挑戦！！"

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100,2)/[5,5] + [43.060, 141.354],
    columns=['lat', 'lon']
)

st.map(df)

st.table(df.style.highlight_max(axis=1))