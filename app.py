import streamlit as st
import pandas as pd


st.title("$$Streamlit Demo$$")


st.write("Hi I am streamlit")

x=st.text_input("type name")

st.write('name is ',x.upper())

df=pd.read_csv('data.csv')

st.table(df)

st.area_chart(data=df)

st.line_chart(data=df)

l1=['sholay','deewar','agneepath','hum']

f=st.radio("select one from the list",l1)

st.write("U selected ",f)

r=st.selectbox("select one ",l1)

st.write("U selected ",r)

r1=st.multiselect("select more ",l1)

st.write("U selected ",r1)

agree = st.checkbox('I agree')

st.write(type(agree))

if agree:
    st.write('Great!')

