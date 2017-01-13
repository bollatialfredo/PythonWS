class Empleado:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Empleado('David', 'Martin', 16400)
emp_2 = Empleado('Alfredo', 'Bollati', 13500)

print("en mano: " +str( emp_1.pay))

print(emp_1.fullname())
print(Empleado.fullname(emp_2))
