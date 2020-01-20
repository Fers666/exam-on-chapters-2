''' тот же 7 но с коректным выводом'''
n=int(input())
mat=[[0 for i in range (n) ]for j in range (n) ]
ns=0
n1=-1
nm=n
li=0
lj=0
a=0
while a<=1 :
    for j in range(lj,nm) :
        ns+=1
        mat[li][j]=ns
        lj=j
    for i in range(li + 1, nm):
        ns += 1
        mat[i][lj] = ns
        li = i
    for j in range(lj - 1, n1, -1):
        ns += 1
        mat[li][j] = ns
    n1 += 1
    lj = n1
    for i in range (li-1,n1,-1) :
        ns+=1
        mat[i][lj]=ns
        li=n1
    li+=1
    lj+=1
    nm-=1

    if ns==((n*n)-1) :
        mat[li][lj]=n*n
        a=2

for i in range(n):
    for j in range (n) :
        print(mat[i][j],end=' ')
    print()