I=open('input.txt')
O=open('output.txt','w')
n=int(I.readline())
has=set()
for i in I.readline().split():
    if i not in has:
        has.add(i)
    else:
        O.write(i)
        O.close()
        I.close()
        exit()
