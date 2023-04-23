# class - define your own data-type - used in 99% of coding languages
# to represent the example of student, create a class for a student is the same as making "student" a data-type

class Student: # classes model real world objects
    # define atributes about Student
    def __init__(self, name, major, gpa, is_on_probation): #initialize function - map out attributes for student
        self.name = name #attribute of name #self is the class name "Student"
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
