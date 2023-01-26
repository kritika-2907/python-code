class Student:
    def __init__(self):
        self.name=input("Enter the name: \n")
        self.age=input("Enter the age: \n")
        self.marks=[]

    def accept(self):
        che=input("Enter the marks for chemistry: ")
        phy=input("Enter the marks for physics: ")
        math=input("Enter the marks for maths: ")
        self.marks.append(che)
        self.marks.append(math)
        self.marks.append(phy)

    def display(self):
        print("NName: "+self.name)
        print("Age: "+self.age)
        print(self.marks)


print("Student 1: \n")
s=Student()
s.accept()
s.display()

print("Student 2: \n")
s1=Student()
s1.accept()
s1.display()