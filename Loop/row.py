# num=int(input("enter no."))
# row=5
# while row <=num:
#     star=row
#     while star>0:
#         print(" * ", end=" ")
#         star=star-1
# print("shshhs")

num=int(input("enter no."))
col=1
while col<=num:
    row=1
    while row<col:
        print(row, end=" ")
        row+=1
        print()
    k=col
    while k>0:
        print(k, end="")
        k+=1
        print()
    col+=1
    