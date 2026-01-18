n=int(input("enter a number"))
temp=n
while n>0:
    digit=n%10
    sum+=digit*digit*digit
    n=n//10
if temp==sum:
 print("ams")
else:
 print("not ams")
