# n=int(input("enter no"))
# i=2
# c=0
# while i<=n:
#     if n%i==0:
#         c=1
#         break
#     i+=1
# if c==0:
#     print("it is a prime no.")
# else:
#     print("it is not a prime no.")

num=int(input("enter no."))
a=1
c=0
while a<=num:
    if num%a==0:
        c+=1
    a+=1
if c==2:
    print(num,"it is a prime no.")
else:
    print(num,"it is not prime no.")
