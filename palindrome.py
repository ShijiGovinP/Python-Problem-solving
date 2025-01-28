n=int(input("enter the value:"))
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=(sum*10)+rem
    n=n//10
if(temp==sum):
    print("palindrome")
else:
    print("not palindrome")
