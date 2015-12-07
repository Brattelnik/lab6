I=open('input.txt')
O=open('output.txt','w')
N=int(I.readline())
free=0
fives=0
s=list(map(int, I.readline().split()))
for i in s:
    if i==5:
        free+=1
    else:
        d=(i-5)//5
        if free>0:
            if free>=d: d,free = 0, free-d
            else: d,free = d-free, 0
        fives+=d
O.write(str(fives))
O.close()
I.close()
