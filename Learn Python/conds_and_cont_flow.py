# comparators
# boolean operators
# conditional statements


# conditionals False and True but be capital
x = True

print (x)

# and, or, must be lower-case
print ("cat" == "dog" or "cat" == "cat")


# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 70 <= grade <= 79:
        return "C"
    elif 65 <= grade <= 69:
        return "D"
    else:
        return "F"


# This should print an "A"
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)