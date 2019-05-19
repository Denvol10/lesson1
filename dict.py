# Словари
product = {
    'name': 'iphone Xs',
    'stock': 24,
    'price': 65432.1
}
print(product)

# Длина словаря
print()
print(len(product))

# Добавление элемента в словарь
''' Элементы словаря можно добавлять и изменять обратившись по названию
ключа. Если такой ключ есть - значение будет обновлено. Если ключа нет
он будет создан.
'''

product['memory'] = 64
print()
print(product) # {'name': 'iphone Xs', 'stock': 24, 'price': 65432.1, 'memory': 64}
product['stock'] = 10
print(product) # {'name': 'iphone Xs', 'stock': 10, 'price': 65432.1, 'memory': 64}

# Получение значения из словаря
print()
print(product['name']) # iphone Xs

# Безопасное обращение по ключу
''' Если вы обратитесь к ключу, которого не существует, программа выдаст
ошибку. Если неизвестно, есть ли ключ в словаре, к нему можно обратиться
через метод .get()
'''
print()
print(product.get('name')) # iphone Xs
print(product.get('discount')) # None
print(product.get('discount', 5)) # 5

# Удаление элемента из словаря
''' С помощью функции del() можно удалить элемент по названию
ключа. Если такого элемента нет - будет ошибка'''
print()
del product['memory']
print(product) # {'name': 'iphone Xs', 'stock': 10, 'price': 65432.1}
#del product['discount'] # KeyError: 'discount'

# Объединение словарей и списков
'''списки и словари можно складывать друг в друга, получая структуры
данных, которые отражают вашу предметную область:'''
print()
phones = ['iphon Xs', 'Samsung Galaxy S10', 'Xiaomi mi8']
product['recomend'] = phones
print(product) # {'name': 'iphone Xs', 'stock': 10, 'price': 65432.1, 'recomend': ['iphon Xs', 'Samsung Galaxy S10', 'Xiaomi mi8']}
print(product['recomend']) # ['iphon Xs', 'Samsung Galaxy S10', 'Xiaomi mi8']
print(product['recomend'][1]) # Samsung Galaxy S10
product['recomend'].append('iPhone 7')
print(product['recomend']) # ['iphon Xs', 'Samsung Galaxy S10', 'Xiaomi mi8', 'iPhone 7']

# Список словарей
print()
stock = [
{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65000},
{'name': 'iPhone 7', 'stock': 10, 'price': 40000, 'recomend': ['iphon Xs', 'Samsung Galaxy S10', 'Xiaomi mi8']},
{'name': 'Xiaomi mi8', 'stock': 5, 'price': 35000}
]
print(stock[0]) # {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65000}
print(stock[0]['name']) # iPhone Xs Plus
print(stock[1]['recomend']) # ['iphon Xs', 'Samsung Galaxy S10', 'Xiaomi mi8']
print(stock[0]['price']) # 65000
stock[0]['price'] += 10000
print(stock[0]['price']) # 75000

# Задание
print()
weather = {'city': 'Moscow', 'temperature': '20'}
print(weather['city'])
weather['temperature'] = str(int(weather['temperature']) - 5)
print(weather)

print(weather.get('country'))
print(weather.get('country', 'Россия'))
weather['date'] = '27.05.2019'
print(weather)
print(len(weather))