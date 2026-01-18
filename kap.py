n=int(input("enter a number"))
sum=0
sq=n*n
temp=n
digits=0
while temp>0:
    digits+=1
    temp=temp//10
divisor=10**digits
right=sq%divisor
left=sq//divisor
sum=left+right
if sum==n:
 print("kap")
else:
 print("not kap")
