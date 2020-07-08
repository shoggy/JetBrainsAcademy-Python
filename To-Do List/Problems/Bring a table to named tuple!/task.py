from collections import namedtuple

student_tuple = namedtuple('Student', ['name', 'age', 'department'])
alina = student_tuple('Alina', '22', 'linguistics')
alex = student_tuple('Alex', '25', 'programming')
kate = student_tuple('Kate', '19', 'art')

print(alina)
print(alex)
print(kate)
