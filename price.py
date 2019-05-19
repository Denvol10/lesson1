def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('максимальная скидка не может быть больше 99%')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

product = {
'name': 'Samsung Galaxy S10',
'stock': 8,
'price': 50000.0,
'discount': 10,
'max_discount': 99
}
print(product)
print('Цена со скидкой телефона', \
    product['name'], 'составит', \
    discounted(product['price'], product['discount']))

'''Помимо обязательных позицтонных аргументов, мы можем задавать
необязательные именованные. Они отличаются тем, что у них есть
значения по-умолчанию. Например, можно датьт возможность управлять
максимальной скидкой'''
print('Цена со скидкой телефона', \
    product['name'], 'составит', \
    discounted(product['price'], product['discount'], product['max_discount']))