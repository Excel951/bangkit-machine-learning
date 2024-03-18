import streamlit as st

# markdown
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# title
st.title('Belajar Analisis Data')

# header
st.header('Pengembangan Dashboard')

# subheader
st.subheader('Pengembangan Dashboard')

# caption
st.caption('Copyright (c) 2024')

# code
code = """
def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

# text
st.text('Halo, calon praktisi data masa depan.')

# latex
# used to retrieve the mathematical expression
st.latex(r"""
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^{n}}{1-r}\right)
         """)