n=int(input())
A=input().split()
for i in range(len(A)):
    A[i]=int(A[i])
for i in range (n):
    D=A[i]
    for j in range(i+1,n):
        C=A[i]
        if D==C:
            z=D
print(z)            
        
