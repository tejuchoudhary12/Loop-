a=int(input("enter no."))
b=int(input("enter no."))
while a%b !=0:
    r=a%b
    a=b
    b=r
if b==r:
    print(b)


