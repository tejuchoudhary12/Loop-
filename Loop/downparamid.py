i=1
n=int(input("enter the no. of rows"))
while n>0:
    s=1
    while s<i:
        print(" ", end=" ")
        s+=1
    j=1
    while j<=(n*2)-1:
        print("*", end=" ")
        j+=1
    print()
    i+=1
    n-=1
