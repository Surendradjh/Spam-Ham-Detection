import streamlit as st
import pickle

st.title('E-Mail Spam Detection')
with open(r"spam_detection.pkl",'rb') as file:
    model=pickle.load(file)

with open(r"Text_converter.pkl","rb") as file:
    tr=pickle.load(file)

E_mail=st.text_input("Enter E-Mail Title")
if st.button('Predict'):
    a=tr.transform([E_mail])
    st.write(a)
    a=model.predict(a)
    if a == 'ham':
        st.write("It's not Spam message")
    else:
        st.write("It's a spam Message please avoid this Message ")
