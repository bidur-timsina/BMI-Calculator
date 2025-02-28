import streamlit as st
from bmi_operation import bmi_calculate, bmi_to_remarks


st.write("<h1> BMI Calculator by Bidur Timsina </h1>" , unsafe_allow_html=True)

weight = st.text_input("Enter Your Weight in KG", key="weight", max_chars=5,value="70")

hight = st.text_input("Enter Your Height in CM", key="height", max_chars=5,value="170")



if st.button("Calculate BMI",help="Click to calculate BMI",type="secondary"):
    bmi = bmi_calculate(float(weight), hight)
    bmi_remarks = bmi_to_remarks(bmi)
    
    st.status(f"Your BMI is {bmi} ---> {bmi_remarks}",expanded=True, state="complete")

