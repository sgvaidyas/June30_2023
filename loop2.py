num1 = int(input("Enter num1 = "))
num2 = int(input("Enter num2 = "))
if num1>num2:
    print(num1," is greater than ", num2)
    while(num2<=num1):#12<=33
        print(num2)   #12
        num2 += 1   #num2=num2+1
elif num1==num2:
    print(num1,"equal to ",num2)
else:
    print(num2," is greater than ", num1)
        #11<=33
    while(num1<=num2):
        print(num1)
        num1 += 1  #num1=num1+1

