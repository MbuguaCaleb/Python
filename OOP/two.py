class Employee:

    raise_amount=1.04
    num_of_emps=0

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last + '@company.com'

        """no need for self as nothing is overridden"""
        """A Class variable with the name of the class"""

        Employee.num_of_emps+=1

    """first agunemt for the instance is always self"""
    """class methods"""
    
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
        


emp_1=Employee('Caleb','Mbugua',50000)
emp_2=Employee('Mercy','Wnjairu',55000)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

"""changing the raise amount class variable from the class"""

#Employee.raise_amount=1.05

emp_1.raise_amount=1.05

print (emp_1.raise_amount)
print (emp_2.raise_amount)


"""dict checks the namespace of a class"""
#print(emp_1.__dict__)
#print(Employee.__dict__)



print(Employee.num_of_emps)

