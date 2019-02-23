class Employee:

    raise_amount=1.04
   
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last + '@company.com'

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
        

"""Inheritance"""

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        #calling parents init method
        self.prog_lang=prog_lang

          
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees =[]
        else:
            self.employees=employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1=Employee('Caleb','Mbugua',50000)
emp_2=Employee('Mercy','Wnjairu',55000)

dev_1=Developer('Caleb','Mbugua',50000,'Python')
dev_2=Developer('Mercy','Wnjairu',55000,'Java')


mgr_1=Manager('Grace','Miringa',90000,[dev_1])  


print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Developer))
print(issubclass(Manager,Developer))
print(issubclass(Manager,Employee))