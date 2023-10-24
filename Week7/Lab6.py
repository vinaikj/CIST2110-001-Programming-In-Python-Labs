# Lab6
# Author:Jsyant Vinaik
import math

## add in functions from test.py's test statements here to make the pytest work

def calculate_rectangle_area(length, width):
    return length * width

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

def find_maximum(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a

def grade_calculator(grade):
    if grade > 100 or grade < 0:
        return "Invalid Score"
    elif grade == 100 or grade >= 90:
        return "A"
    elif grade < 90 and grade >= 80:
        return "B"
    elif grade < 80 and grade >= 70:
        return "C"
    elif grade < 70 and grade >= 60:
        return "D"
    else:
        return "F"

def main():
    pass



if __name__ == "__main__":
    main()