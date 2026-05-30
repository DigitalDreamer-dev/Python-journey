import streamlit as st
st.title("CALCULATOR")
a=st.number_input("Enter 1st Number: ")
b=st.number_input("Enter 2nd Number: ")
cols = st.columns(4)        #to create 4 columns using list method
b1=cols[0].button("+")
b2=cols[1].button("-")
b3=cols[2].button("*")
b4=cols[3].button("/")
if b1:
    st.info(a+b)    #info
    st.balloons()
if b2:
    st.success(a-b)     #green
    st.snow()
if b3:
    st.warning(a*b)   #yellow
    st.balloons()
try:
    if b4:
        st.error(a/b)  #red
        st.snow()
except ZeroDivisionError:
    st.write("Cannot divide by zero")

