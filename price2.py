def format_price(price):
	price = int(price)
	return f'Цена: {price} руб.'
price1 = format_price(52.64)
print(price1)