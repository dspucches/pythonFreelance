# object is the actual student with a name, major, gpa, on probation
# Class is the overall template, defines what a "student" is.

from ClassesAndObjects import Student

student1 = Student("Jim", "Business", 3.1, False) # Object is creating a student object - instance of a class
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name)
print(student2.name)
