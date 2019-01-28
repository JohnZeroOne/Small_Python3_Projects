# generic class for any student
class student():

    # give each student a unique ID
    idnum = 0

    # each instance of student must have these
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.idnum = student.idnum
        student.idnum += 1

    # return student's id
    def getidnum(self, idnum):
        return idnum

    # surname
    def lastname(self):
        self.lastname = lastname

    # age of student
    def age(self):
        self.age = age

    # student score
    def gpa(self):
        self.gpa = gpa

    # classes the student takes
    def classes(self):
        self.classes = classes

    # comparing students by attributes
    def __lt__(self, other):
        if self.age == other.age:
            return "Same age"
        elif other.age < self.age:
            return other.age < self.age
        return self.age < other.age

    # printing students and subclasses
    def __str__(self):
        return self.name

# st1 = student("Fred")
# st2 = student("Bob")
# st3 = student("John")
# st4 = student("Rob")
# st5 = student("James")

# st1.age = 19
# st1.classes = ["Geography"]
# st1.classes
# ['Geography']
# st1.classes += ["Science"]
# st1.classes
# ['Geography', 'Science']

# specific graduate inherits from student
class graduate(student):

    def degree(self):
        self.degree = degree

#gd1 = graduate("Marvin")
#gd1.idnum
#2

#gd1.degree = "Masters in Biological studies"
#print(gd1)
#Marvin
#print(gd1.degree)
#Masters in Biological studies
