'''print("hi",end=" ")
print("hello")'''

n = int(input("Enter n ="))
i=n
j=1
while(j<=n//2):
    print(i,j,end=" ")
    i-=1
    j+=1
else:
    if i==j:
        print(i)
