n=int(input("enter the number:"))
count=0
for i in range(1,n):
    if n%i==0:
        count=count+1
if count==1:
    print("prime")
else:
    print("not prime")
