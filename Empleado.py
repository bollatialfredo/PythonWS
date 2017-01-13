class Empleado:

    def __init__(corcho, first, last, pay):
        corcho.first = first
        corcho.last = last
        corcho.pay = pay
        corcho.email = first + '.' + last + '@company.com'


emp_1 = Empleado('David', 'Martin', 16400)
emp_2 = Empleado('Alfredo', 'Bollati', 13500)

print("en mano: " +str( emp_1.pay))
