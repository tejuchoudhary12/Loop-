# i=1
# k=1
# while i<=5:
#     s=1
#     while s<=5:
#         if s<i:
#             print(" ",end=" ")
#         else:
#             print("*  ",end=" ")
#         s+=1
#     k+=2
#     print()
#     i+=1



k=1
i=5
while i<=5:
    s=i-k
    while s<=5:
        if s>0:
            print(" ",end=" ")
        else:
            print("*",end=" ")
        k+=1
    print()
    i-=1


