''' присвоение суммы в двумерный список'''
matr=[[str(1) for i in range(3)] for j in range(3)]
matr[0][0]=sum([matr[0][0],matr[0][1]])
for i in matr :
    print(i)

''' ввод двумерного списка с дальнейшим указание типа переменных '''
while True :
    print('Введите строку разделенную пробелами : ')
    s=str(input())
    if s == 'end' :
        break
    mat.append([int(x) for x in s.split()])