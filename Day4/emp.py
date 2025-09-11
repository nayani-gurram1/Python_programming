class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        print("Manager Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
emp = Employee("Aksh", 100000)
emp.display()
mgr = Manager("Tabu", 150000, "HR")
mgr.display()
