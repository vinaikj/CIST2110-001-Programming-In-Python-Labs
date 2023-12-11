#Lab 9
# Author: Jayant Vinaik

"""_summary_

This lab is designed to create a simple web application using streamlit and create a simple Date counter using datetime.
"""

# 1. We will first need to activate and install streamlit.
# pip install streamlit

# 2. Import streamlit here as st and datetime as dt
import streamlit as st
import datetime as dt


# 3. Create a title for your web application. Streamlit has a function for this called title
st.title("Simple Date Counter")


# 4. Create a subheader for your web application. Streamlit has a function for this called subheader
st.subheader("This is a simple date counter")

# 5. Create a date input for the user to enter a date. Streamlit has a function for this called date_input
# Make sure to save the input into a variable
user_date = st.date_input("Enter a date")


# 6. Create a button for the user to click. Streamlit has a function for this called button
# Make sure to save the button click into a variable
button_clicked = st.button("Click to Count")

# 7. Create a function that will calculate the number of days until the date entered by the user.
# You will need to use the datetime library for this.
# You will need to convert the user input into a datetime object.
# You will need to get the current date and convert it into a datetime object.
# You will need to subtract the current date from the user input date.
# You will need to return the number of days.
# The function should take in a datetime.date as a parameter.
# The function should return an integer.
# The function should be called calculate_days

def calculate_days(user_date):
  # Get the current date
  current_date = dt.datetime.now().date()

  # Calculate the difference between the user input date and the current date
  days_difference = (user_date - current_date).days

  return days_difference


# 8. Create an app function that will run the web application.
# Check if the button has been clicked, then call the calculate_days function and pass in the date entered by the user. Use a try except block to catch any errors.
# Save the result into a variable.
# Print out the result.
def app():
  if button_clicked:
      try:
          result = calculate_days(user_date)
          st.write(f"Number of days until the entered date: {result} days")
      except Exception as e:
          st.error(f"An error occurred: {str(e)}")


# 9. Run the web application by typing streamlit run Lab9.py in the terminal.
# 10. Enter a date in the format of YYYY-MM-DD and click the button.
# 11. Check to see if the number of days until the date entered is correct.
# 12. If the number of days is correct, then you have completed the lab.
# 13. If the number of days is incorrect, then you will need to debug your code.

if __name__ == '__main__':
    app()