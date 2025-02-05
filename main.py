# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st

st.title("Hello, World!")
st.header("Header --> Geeks for Geeks")
st.subheader("subheader --> Geeks for Geeks")
st.text("Text --> Geeks for Geeks")
st.markdown('#Hi')
st.markdown('##Hi')
st.success("Success")
st.info("Information")
st.warning('Warning!')
st.error('Error!')
st.exception(ZeroDivisionError('Div not possible'))
st.help(ZeroDivisionError)
st.write("Range(1,10)")
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)
st.code('x=10\n'
        'for i in range(x):\n'
        '\tprint(i)')
st.checkbox('Male')
st.checkbox('Female')
if(st.checkbox('Adult')):
    st.write("You're an adult!")
st.radio('Select: ', ('Male', 'Female', 'Other'))
radioButton = st.radio('Select :', ('Male', 'Female','Other'))
if(radioButton == 'Male'):
    st.write('Male')
elif(radioButton == 'Female'):
    st.write('Female')