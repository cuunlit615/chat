import os
products = []
#檢查檔案是否存在
if os.path.isfile('input.txt'):
    # 讀取
    print('File exist')
    with open('input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:  # 如果'商品,價格'存在
                continue  # 跳過此物件
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)

else:
    print('File not found \nCreate new file')


#讓使用者輸入
while True:
    name = input('Product name:')
    if name == 'q':
        break
    price = input('Products price:')
    price = int(price)
    # 方法A
    # p = []
    # p.append(name)
    # p.append(price)
    # products.append(p)
    # 方法B
    # p = [name, price]
    # 方法C
    products.append([name, price])
print(products)

#印出購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

#寫入購買紀錄
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
for i in list:

A = []
A = A.add(i)