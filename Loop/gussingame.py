i=5
n=1
a=10
while n<=a:
    s=int(input("enter no."))
    if s==i:
        print("YOU WIN")
        break
    elif s!=i and s<a:
        print(a-s,"remaining chances ")
    else:
        print("you have no chance")
    a-=s