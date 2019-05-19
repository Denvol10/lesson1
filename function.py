# Функции
# Задание 1
def get_summ(one, two, delimiter='&'):
	one = str(one)
	two = str(two)
	return one + delimiter + two
text = get_summ('Learn', 'python')
print(text.upper())