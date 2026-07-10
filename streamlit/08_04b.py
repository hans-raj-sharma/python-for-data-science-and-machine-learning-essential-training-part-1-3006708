import time
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

rows = np.random.randn(1,1)

'Growing Line Chart:'
chart = st.empty()
chart.line_chart(rows)

for i in range(1,100):
  new_row = rows[-1:] + np.random.randn(1,1)
  rows = np.concatenate([rows, new_row], axis=0)
  chart.line_chart(rows)
  time.sleep(0.05)

values = np.random.randn(10)
'matplotlib Line Chart:'
fig, ax = plt.subplots()
ax.plot(values)
st.pyplot(fig)