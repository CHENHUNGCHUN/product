product = []
while True:
    name = input('請輸入商品: ')
    if name == 'q':
        break
    price = eval(input('請輸入商品價格: '))
    p = [name,price]
    product.append(p)
print(product)

for item in product:
    print(item)
