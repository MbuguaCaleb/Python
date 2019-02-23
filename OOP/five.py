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
        
    """There are two dunder methods"""
    """They allow us change how our objects are printed and displayed"""

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname(),self.email)
    
    """Arithmentic dunder add"""
    def __add__(self,other):
       return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1=Employee('Caleb','Mbugua',50000)
emp_2=Employee('Mercy','Wnjairu',55000)

#print(emp_1)
#print(repr(emp_1))
#print(str(emp_1))
#print(emp_1.__repr__())
#print(emp_2.__str__())

#print( emp_1+ emp_2)
print(len('test'))


print('test'.__len__())

print(len(emp_1))


