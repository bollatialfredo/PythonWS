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

    @classmethod #setea el raise_amount de la clase Empleado
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod  #crea un empleado de un string, constructor alternativo
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day): #metodo estatico, no recibe ni clase ni instancia
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

emp_1 = Empleado('David', 'Martin', 16400)
emp_2 = Empleado('Alfredo', 'Bollati', 13500)

import datetime
my_date = datetime.date(2017, 1, 13)
print(Empleado.is_workday(my_date))
