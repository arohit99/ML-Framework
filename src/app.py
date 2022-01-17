import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


plt.style.use('fivethirtyeight')

st.title('ML Framework')

#df = pd.DataFrame({'x':range(1,100), 'y':3*(range(1,100)+5)})
x= list(range(1,101))
y=  [(3 * i) + 5 for i in x]

st.subheader('Sample Plot')
fig,ax = plt.subplots(figsize=(8,5))
ax.plot(x,y)

st.pyplot(fig)


