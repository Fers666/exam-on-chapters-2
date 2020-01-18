'''
минимальное вводимое значение списка
'''
''' 1 способ'''
spisok=[int(i) for i in input().split()]
min=spisok[0]
for x in spisok :
    if min>x :
        min=x
print(min)
''' 2 способ через встроеную функцию'''
spisok=[int(i) for i in input().split()]
print(min(spisok))