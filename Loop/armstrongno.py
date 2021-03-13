num=int(input("enter no."))
sum=0
a=num
len=len(str(num))
while a>0:
    f=a%10
    sum=sum+(f**len)
    a//=10
if num==sum:
    print(num,"its an armstrong no.")
else:
    print(num,"it is not an armsrtong no.")
