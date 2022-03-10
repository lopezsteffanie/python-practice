last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# Indivdual subjects and their grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Gradebook list with subjects and grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# New class and grade
gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])

# Extra credit in visual arts class
gradebook[-1][-1] += 5

# Change to Pass/Fail for poetry
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Full Gradebook
full_gradebook = last_semester_gradebook + gradebook

# Check work
#print(gradebook)
print(full_gradebook)