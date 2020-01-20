'''
Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2n
2
  по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):
'''
''' ввод числа n '''
n=int(input())
mat=[]
mat=[[0 for i in range (n) ]for j in range (n) ]
''' 
ns счетчик всех значений матрицы 
n1 (индекс первого элемента ) 
nm предельное значени ( n но изменяемый ) 
li,lj координа переменных ( для спирали) 
a граница цикла while
'''
ns=0
n1=-1
nm=n
li=0
lj=0
a=0
while a<10 :
    ''' верхняя строка спирали '''
    for j in range(lj,nm) :
        ns+=1
        mat[li][j]=ns
        lj=j
    ''' правый столбик спирали'''
    for i in range (li+1,nm) :
        ns+=1
        mat[i][lj]=ns
        li=i
    ''' нижняя строка спирали'''
    for j in range(lj-1,n1,-1):
        ns+=1
        mat[li][j]=ns
    n1+=1
    lj=n1
    ''' левый столбец спирали'''
    for i in range (li-1,n1,-1) :
        ns+=1
        mat[i][lj]=ns
        li=n1
    li+=1
    lj+=1
    nm-=1
    if ns==((n*n)-1) :
        mat[li][lj]=n*n
        a=10


for i in mat:
    print(i)

