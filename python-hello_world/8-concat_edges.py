#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
str = str[56:85]  # slice only the "object-oriented programming" part
str += " with Python"  # add " with Python"
print(str)
