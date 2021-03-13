n=int(input("enter no"))
a=n%10
b=(n//10)%10
c=(n//10)//10
while n<1000:
    print(a*100+b*10+c*1)
    break