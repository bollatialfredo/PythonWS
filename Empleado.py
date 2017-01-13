class Empleado:

    num_of_emp = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Empleado.num_of_emp += 1

    @property
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


    def __repr__(self):
        return "Empleado('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
class Developer(Empleado):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


emp_1 = Developer('David', 'Martin', 16400, 'Python')
emp_2 = Empleado('Alfredo', 'Bollati', 13500)

emp_1.first = 'Juan'

print(emp_1.fullname)
