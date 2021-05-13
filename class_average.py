

"""
This program will have a list that stores 5 numbers that capture user input 5 times for their grades.
Each time user inouts a number we will add to the list


We will sort the list by ascending and then splice the items starting at index 2

Once we capture the 3 highest numbers from the list we will sum and divide by 3

It will output a message to the user
"""

"""
create list
capture input
append.number to list # times 5

capture input
append.number to list

capture input
append.number to list

capture.... etc.

print message 
"""


grades = []

grade = input("Enter the 1st grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input("Enter the 4th grade: ")
grades.append(float(grade))

grade = input("Enter the 5th grade: ")
grades.append(float(grade))

grades.sort()
grades = grades[2:]
grades = sum(grades)
result = grades / 3


print("Average Grade {0:.2f}%".format(result))
