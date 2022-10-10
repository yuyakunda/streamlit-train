from tkinter import Image
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('DataFrame')

img = Image.open('IMG_3102.jpg')
st.image(img, caption='field map', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[5,5] + [43.060, 141.354],
#     columns=['lat', 'lon']
# )

# st.map(df)

#st.table(df.style.highlight_max(axis=1))