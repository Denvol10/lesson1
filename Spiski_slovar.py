# Списки - Lists
# Словари - Dictionaries

phones = ['iphon Xs', 'Samsung Galaxy S10', 'Xiaomi mi8']
print(phones)
print(len(phones)) # 3

# Добавление элемента в конец списка с помощью метода .append()
phones.append('iphon Xs')
print(len(phones)) # 4

# Подсчет количества элементов в списке
print(phones.count('iphon Xs'))
print(phones.count('iPhone 6'))

# Работа с отдельными элементами
print(phones[1]) # 'Samsung Galaxy S10'
print(phones[3]) # 'iphon Xs'
print(phones[-1]) # 'iphon Xs'

# Срезы списка
print(phones[1:3]) #['Samsung Galaxy S10', 'Xiaomi mi8']
print(phones[:2]) #['iphon Xs', 'Samsung Galaxy S10']
print(phones[-1]) #iphon Xs

# Поиск индекса элемента
print(phones.index('Samsung Galaxy S10')) # 1

# Сортировка списка
phones.sort()
print(phones)

# Оператор in
print('Samsung Galaxy S10' in phones) # True
print('Nokia 3310' in phones) # False

# Удаление элементов
del phones[1] # удаление по индексу
print(phones)
phones.remove('Samsung Galaxy S10')
print(phones)

# Задание
print()
lst = [3, 5, 7, 9, 10.5]
print(lst)
lst.append('Python')
print(lst)
print(len(lst))
print(lst[0])
print(lst[-1])
print(lst[2:5])
lst.remove('Python')
print(lst)