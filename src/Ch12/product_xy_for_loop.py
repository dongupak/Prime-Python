
# 코드 12-23 : 두 리스트를 곱하여 새 리스트를 생성하는 코드


product_xy = []
for x in [1, 2, 3]:     # 이중 for 루프를 통해 두 리스트 원소의 곱을 모두 구함
    for y in [2, 4, 6]:
        product_xy.append(x * y)

print(product_xy)
