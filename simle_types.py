# Целые числа
a = 2
b = 3
c = a + b
print(c)

# Вещественные числа
a = 2.5
b = 3.1
c = a + b
print(c)

a = 2.5
b = 0.5
c = a - b
print(c) # 2.0

# В python3 в результате деления всегда получаем вещественное число
a = 2
b = 2
c = a / b
print(c)

# Логический тип (bool)
# True - истина
# False - ложь
a = 3
b = 0
c = a != b
print(c) #False

# Строки (string)
a = 'Привет'
b = 'Мир'
c = a + ' ' + b + '!'
print(c)

# Форматирование строк (метод формат)
a = 'Привет'
b = 'Мир'
c = '{} {}!!!'.format(a, b)
print(c)
c = 2
d = '{} {}{}!'.format(a, b, c)
print(d)

user = 'Python'
c = 'Привет {name}!'.format(name = user)
print(c)

# f-строки начиная с версии python 3.6
user = 'Миша'
b = f'Привет {user}!'
print(b)

# Подробно о форматировании строк pyformat.info

# Длина строки
a = 'Привет'
b = 'Мир'
c = f'{a} {b}!'
d = len(c)
print(d)

# Приведение строк
a = 'Привет'.upper()
print(a) # ПРИВЕТ
b = 'Привет'.lower()
print(b) # привет
c = 'python'.capitalize()
print(c) # Python

# удаление пробелов из начала и конца строки
a = '  Привет   '
print(a.strip()) # Привет

# Замена в строке

a = 'Прив3т т3б3'.replace('3', 'e')
print(a) # Привет тебе
a = 'ПриветЫ'.replace('Ы', '')
print(a) # Привет

# Объединение методов
a = 'ПРивет приветЫ'.lower().capitalize().replace('ы', '')
print(a) # Привет привет

a = 'Привет мир'.replace('мир', 'Python')
print(a)

# Разбиение строки в список
a = 'learn.python.ru'
b = a.split('.') # ('.') - указываем по какому символу разбивать
print(b) # ['learn', 'python', 'ru']

# Количество стлов в предложении
a = 'Предлжение из      нескольких слов 123'
b = a.split() # разбиение по пробелам (воспримет, если несколько пробелов)
print(b)
print(len(b))

# Специальный тип данных None

''' None - это отдельный тип данных, который обозначает "отсутствие значения".
Чаще всего мы будем сталкиваться с None, когда какая-то функция не вернула
значения. Мы можем провериить на None при помощи ключевого слова is
'''
a = None
b = 0
print(a is None) # True
print(b is not None) # True

# Определение типа переменной

a = 2 # Какого типа a?
print(type(a)) # <class 'int'>
b = '2.0' # Какого типа b?
print(type(b)) # <class 'str'>
c = 2.0 # Какого типа c?
print(type(c)) # <class 'float'>
d = True
print(type(d)) #<class 'bool'>
e = None
print(type(e)) # <class 'NoneType'>

# Пользовательский ввод
name = input('Введите ваше имя: ')
print(f'Привет, {name}!')

age = input('Сколько Вам лет? ') # из input всегда приходит строковый тип данных
print(type(age))
age = 2019 - int(age)
print(f'Ваш год рождения {age}')

# Приведение типов
# int() приведение к целому цислу
# float() приведение к вещественному числу
# bool() приведение к логическому выражению
# все что не равно 0 и не None приведет к True
a = bool(5) # True
print(a)
a = bool('') # False
print(a)
a = bool(0) # False
print(a)
a = bool(None) # False
print(a)
# str() приведение к строке

# Практика числа
v = int(input('Введите число от 1 до 10: '))
a = v + 10
print(f'Число {a} на 10 больше введенного {v}')

# Практика строки
name = input('Введите ваше имя: ')
name = name.upper()
print('Привет, {}! Как дела?'.format(name))

# Практика приведение типов
print(float('1')) # 1.0
#print(int('2.5')) # ValueError: invalid literal for int() with base 10: '2.5'
print(bool(1)) # True
print(bool('')) # False
print(bool(0)) # False