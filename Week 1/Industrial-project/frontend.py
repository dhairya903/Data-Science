import streamlit as st
import requests

st.header("Week 1 project")
st.subheader("Invoice reader")

filename = st.text_input("Enter file name: ")
print(filename)
if filename != '':
    response = requests.get(f"http://127.0.0.1:8000/total-amount/{filename}")
    decoded_json = response.json()
    if response.status_code == 404:
        message = decoded_json['detail']
        st.error(message)
    elif response.status_code == 200:
        message = decoded_json['Total amount']
        message = 'The total amount of invoice is :  ' + str(message)
        st.success(message)
    # st.write(response.json())