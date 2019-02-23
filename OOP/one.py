"""creating and instanciating classes"""
"""enable us to reuse class attributes"""
class Employee:

    """all other methods receive the instance as the first argument automatically"""
    """initialising class attributes"""

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last + '@company.com'

    """first agunemt for the instance is always self"""
    """class methods"""
    
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    
emp_1=Employee('caleb','Mbugua',25000)
emp_2=Employee('Ruth ','Wamboi',15000)

#print(emp_1.email)
#print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())

"""calling the method on the class:using the class"""

print (Employee.fullname(emp_1))
print (Employee.fullname(emp_2))





   





