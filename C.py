n=int(input())
min=1000000
A=input().split()
for i in range(len(A)):
    A[i]=int(A[i])
for i in range (len(A)):
    B=A[i]
    for j in range(i+1,len(A)):
        C=A[j]
        if B<0 and C>0 and B==-C:
            z=j-i
            if z<min:
                min=z
print(min)                
            
