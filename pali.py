n=int(input("enter a number"))
rev=0
temp=n
while n>0:
    i=n%10
    rev=rev*10+i
    n=n//10
if rev==temp:
 print("pali")
else:
  print("not pali")
  