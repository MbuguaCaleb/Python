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
        
    """Used for mutiple constructors"""
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount

    """class method as an alternative constructor"""
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        """calling employee via cls thus acting as an alternative constructor"""
        return cls(first,last,pay)

    """Have logical connection with the class but/
    you dont access the instance anywhere within the class"""

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False     
        return True

    
"""for class methods"""

#emp_1=Employee('Caleb','Mbugua',50000)
#emp_2=Employee('Mercy','Wnjairu',55000)

#emp_str_1='John-Doe-70000'

#first,last,pay=emp_str_1.split('-')

#new_emp_1=Employee(first,last,pay)

#new_emp_1=Employee.from_string(emp_str_1)
#print(new_emp_1.email)
#Employee.set_raise_amt(1.05)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

"""for static methods"""

import datetime
my_date = datetime.date(2019,2,23)

print(Employee.is_workday(my_date))