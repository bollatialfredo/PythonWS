from Empleado import Empleado
from Empleado import Developer

class Manager(Empleado):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

mg_1 = Manager('Paula', 'Dabos', 20000, [])

dev_1 = Developer('David', 'Martin', 13000, 'JavaScript')
dev_2 = Developer('Alfredo', 'Bollati', 12000, 'Python')

mg_1.add_emp(dev_1)
mg_1.add_emp(dev_2)
mg_1.print_emps()
print('----')
mg_1.remove_emp(dev_1)
mg_1.print_emps()

print(isinstance(mg_1, Manager))
print(isinstance(mg_1, Empleado))
print(isinstance(mg_1, Developer))
print('---')
print(issubclass(Manager, Empleado))
print(issubclass(Manager, Developer))
