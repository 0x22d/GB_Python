#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой
'''
name = input('Введите имя ')
surname = input('Введите фамилию ')
year = int(input('Введите год рождения '))
city = input('Введите город ')
email = input('Введите email ')
telephone = input('Введите номер ')
'''
def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])

print(my_func(surname='Malinovskaya', name='Alena', year='1998', city='Kaliningrad', email='0x22d@beanetto.ru',
              telephone='8-991-114-38-28'))