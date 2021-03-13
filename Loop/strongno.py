sum=0
num=int(input("enter no."))
a=num
while num>0:
    i=1
    f=1
    r=num%10
    while i<=r:
        f*=1
        i+1
    sum+=f
    num//=10
if sum==a:
    print("strong no.")
else:
    print("not strong no.")