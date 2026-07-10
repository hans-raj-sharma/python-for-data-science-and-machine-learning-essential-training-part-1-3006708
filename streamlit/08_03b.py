import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

col_names = ['column1','column2','column3']

data = pd.DataFrame(np.random.randint(30, size=(30, 3)), columns=col_names)

'line graph:'
st.line_chart(data)

"bar graph:"
st.bar_chart(data)

animals = ['cow','dog','cat']
heights = [150,90,60]

'pie chart:'
fig, ax = plt.subplots()
ax.pie(heights, labels=animals)

st.pyplot(fig)