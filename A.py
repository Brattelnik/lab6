Irga=open('input.txt')
Orex=open('output.txt','w')
n=int(Irga.readline())
mama=set()
for i in Irga.readline().split():
    if i not in mama:
        mama.add(i)
    else:
        Orex.write(i)
        Orex.close()
        I.close()
        exit()
