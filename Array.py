Courses= [ "MIT", "Cybersecurity","Datascience"]

print(Courses)

#Accessing an element in an array
print(Courses[1])

# Looping through an array
for course in Courses:
    print(course)
    # Adding an element in an array
Courses.append("Android development")
print(Courses)

# Removing an  element in an array
Courses.remove("MIT")
print(Courses)