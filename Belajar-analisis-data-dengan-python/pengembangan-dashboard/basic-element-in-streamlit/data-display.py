import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# dataframe
# retrieve dataframe to streamlit
st.dataframe(data=df, width=500, height=150)

# table
st.table(data=df)

# metric
st.metric(label='Temperature', value="28 °C", delta="1.2 °C")

# json
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})