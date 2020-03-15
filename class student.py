class student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        print ('name:', self.name)
        print ('rollno:', self.rollno)


name = str(input('please enter your name:'))
rollno = int(input('please enter your rollno:'))
s1 = student(name, rollno)
s1.display()
