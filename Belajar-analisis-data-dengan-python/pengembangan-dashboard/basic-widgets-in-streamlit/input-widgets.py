import datetime
import pandas as pd
import streamlit as st

# input
name = st.text_input(label='Nama Lengkap', value='')
st.write('Nama: ', name)

# text area
text = st.text_area('Feedback')
st.write('Feedback: ', text)

# input number
number = st.number_input(label='Umur')
st.write('Umur: ', number, ' tahun')

# date input
date = st.date_input(label='Tanggal Lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal Lahir: ', date)

# file uploader
uploaded_file = st.file_uploader('Choose a CSV file to upload')

if uploaded_file:
    # read csv file
    df = pd.read_csv(uploaded_file)
    # write data in web
    st.dataframe(df)
    
# camera input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)