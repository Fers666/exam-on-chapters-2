''' ввод двумерного массива !!! '''
mat=[]
while True:
    s=input('Введите строку разделенную пробелами')
    if s=='end':
        break
    row=[int(x) for x in s.split()]
    mat.append(row)
''' Второй способ '''
    mat = []
    while True:
        s = input('Введите строку разделенную пробелами')
        if s == 'end':
            break
        mat.append(s.split())
    print(mat)


