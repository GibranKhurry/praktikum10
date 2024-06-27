# import the streamlit library
import streamlit as st
from datetime import datetime

# give a title to our app
st.title('Age Calculator')

# TAKE DATE OF BIRTH INPUT
date_of_birth = st.date_input('Enter your date of birth')

# function to calculate age
def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# calculate age when the user enters a date
if date_of_birth:
    age = calculate_age(date_of_birth)
    st.write(f'You are {age} years old.')
else:
    st.write('Please enter your date of birth')

# exception handling for invalid inputs
try:
    if date_of_birth > datetime.today().date():
        st.write('Invalid date! Please enter a date in the past.')
except:
    st.write('Error! Please enter a valid date.')
