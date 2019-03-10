# function to calculate average mathematically
def average(numbers):
  total = float(sum(numbers))
  return total/len(numbers)

# input student dictionary and get avg of hw, quizzes, and tests
def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return homework*.10 + quizzes*.30 + tests*.60

def get_class_average(class_list):
    results = []
    for val in class_list:
        #stud_avg = get_average(val)
        #results.append(stud_avg)
        results.append(get_average(val))
    print ("results is: %s" % results)
    return average(results)

def get_letter_grade(score):
  if (score >= 90):
    return "A"
  elif (90 > score and score >= 80):
    return "B"
  elif (80 > score and score >= 70):
    return "C"
  elif (70 > score and score >= 60):
    return "D"
  else:
    return "F"

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}

alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

class_list = [lloyd, alice, tyler]

print (get_letter_grade(get_average(lloyd)))
print (get_class_average(class_list))