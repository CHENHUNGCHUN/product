data=[]
with open('product.csv','r',encoding='utf-8') as f:
    for i in f:
        if '商品,價格' in i:
            continue
        a,b = i.strip().split(',')
        _=[a,b]
        data.append(_)

while True:
    name = input('請輸入商品: ')
    if name == 'q':
        break
    price = eval(input('請輸入商品價格: '))
    p = [name,price]
    data.append(p)
print(data)

# with open('product.txt','a') as f:
#     for product in data:
#         f.write(product[0] + ',' + str(product[1]) + '\n')

with open('product.csv','w',encoding='utf-8') as f:
    f.write('商品,價格\n')
    for product in data:
        f.write(product[0] + ',' + str(product[1]) + '\n')
