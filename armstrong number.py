n=int(input("enter a number:"))
sum=0
temp=n
while(temp>0):
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if (n== sum):
    print(" an armstrong number")
else:
    print("not an armstrong number")
