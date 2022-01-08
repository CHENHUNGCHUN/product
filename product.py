products = []
while True:
    name = input('請輸入商品: ')
    if name == 'q':
        break
    price = eval(input('請輸入商品價格: '))
    p = [name,price]
    products.append(p)
print(products)

for item in products:
    print(item)

# with open('product.txt','a') as f:
#     for product in products:
#         f.write(product[0] + ',' + str(product[1]) + '\n')

with open('product.csv','a',encoding='utf-8') as f:
    f.write('商品'+','+'價格'+'\n')
    for product in products:
        f.write(product[0] + ',' + str(product[1]) + '\n')