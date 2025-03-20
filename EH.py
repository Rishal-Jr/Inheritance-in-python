class Person(object):
    def __init__(self,name,Idnumber):
        self.name=name
        self.Idnumber=Idnumber

    def display(self):
        print(self.name)
        print(self.Idnumber)

class Employee(Person):
    def __init__(self,name,Idnumber,salary,post):
        self.salary=salary
        self.post=post 
        Person.__init__(self,name,Idnumber,) 

    def d1(self):
        print(self.salary)
        print(self.post)
       

a=Employee("Rishal",886677,200000,"manager")
a.display()
a.d1()