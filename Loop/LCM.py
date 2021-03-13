a=int(input("enter 1st no."))
b=int(input("enter 2nd no."))
if a>b:
    m=a 
else:
    m=b
while 1:
    if m%a==0 and m%b==0 :
        print("LCM is: ",m)
        break
    m+=1