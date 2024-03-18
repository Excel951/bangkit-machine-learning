import streamlit as st

# button
if st.button('Say Hello'):
    st.write('Hello there!')

# checkbox
agree = st.checkbox('I agree')

if agree:
    st.write('Welcome to MyApp!')

# radio button
radio_genre = st.radio(
    label="What's your favorite movie genre?",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

# select box
selectbox_genre = st.selectbox(
    label="What's your favorite movie genre?",
    options=('Comedy', 'Drama', 'Documentary'),
)

# multi-select box
multi_genre = st.multiselect(
    label="What's your favorite movie genre?",
    options=('Comedy', 'Drama', 'Documentary'),
)

# slider box
values = st.slider(
    label='Select a range of values',
    min_value=0,
    max_value=100,
    value=(0,100)
)
st.write('Values:', values)