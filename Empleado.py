class Empleado:

    num_of_emp = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Empleado.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
emp_1 = Empleado('David', 'Martin', 16400)
emp_2 = Empleado('Alfredo', 'Bollati', 13500)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
Empleado.raise_amount = 1.05
print(Empleado.raise_amount)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
emp_1.raise_amount = 1.08
print(emp_1.raise_amount)
print(Empleado.raise_amount)
print(emp_2.raise_amount)

print(emp_1.num_of_emp)

print(Empleado.num_of_emp)

#print(emp_1.fullname())
#print(Empleado.fullname(emp_2))
