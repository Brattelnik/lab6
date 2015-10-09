n=int(input())
A=input().split()
for i in range(len(A)):
    A[i] = int(A[i])
n=sum(A)
Summa5=0
max=0
summaprik=0
for i in range (len(A)):
    if A[i]==5:
        Summa5+=5
for i in range (len(A)):
    if A[i]==5:
        summaprik-=5
    else:
        summaprik+=(A[i]-5)
    if summaprik>(n-5*len(A)-Summa5) and summaprik>max:
        max=summaprik
if max==0:
    if (n-5*len(A)-Summa5)>0:
        print((n-5*len(A)-Summa5)//5)
    else:
        print("0")
else:
    print(max//5)