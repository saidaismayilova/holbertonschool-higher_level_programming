#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[56:85]  # slice only the "object-oriented programming" part
str += " with Python"  # add " with Python"
print(str[56:64] + "-" + str[65:75] + str[75:85] + " with Python")
