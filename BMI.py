

import streamlit as st

st.title("BMI calculator")

#Input

weight = st.number_input("Enter your weight in KG", step = 0.1)

height = st.number_input("Enter your height in Meters", step = 0.02)

def calculate_bmi():
    bmi = weight/(height)**2
    bmi_thresholds = [18.5, 25, 30, 35, 40, 45]
    level_labels = ['Underweight','Low Risk','Moderate Risk','High Risk','Obese class 1', 'Obese class 2', 'Obese class 3', 'Error']
    if bmi <= bmi_thresholds[0]:
        level = level_labels[0]
    elif bmi <= bmi_thresholds[1]:
        level = level_labels[1]
    elif bmi <= bmi_thresholds[2]:
        level = level_labels[2]
    elif bmi <= bmi_thresholds[3]:
        level = level_labels[3]
    elif bmi <= bmi_thresholds[4]:
        level = level_labels[4]
    elif bmi <= bmi_thresholds[5]:
        level = level_labels[5]
    elif bmi <= bmi_thresholds[6]:
        level = level_labels[6]
    else:
        level = level_labels[7]
        if level is level_labels[7]:
            st.error(f"Inhuman Statistics, Value is invalid")
        else:
            st.success(f"Your BMI is {bmi}. You are at {level}")

button = st.button("Calculate BMI")
if button:
    calculate_bmi()
