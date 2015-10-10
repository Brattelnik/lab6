input = open('input.txt', 'r')
A=[] 
B=intinput.readlines() 
n=int(B[0]) 
A=A+list(map(int, B[1].split())) 
for i in range (n):
    D=A[i]
    for j in range(i+1,n):
        C=A[i]
        if D==C:
            z=D
output = open('output.txt', 'w')
print(z,file=output)
input.close()
output.close()
