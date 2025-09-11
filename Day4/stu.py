class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll number:",self.roll_no)
        print("Marks:",self.marks)

stu=Student("tabu",6724,97)
stu.display()
stu1=Student("aksh",6707,95)
stu1.display()