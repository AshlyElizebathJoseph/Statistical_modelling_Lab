l=int(input("Enter the value of lamda: "))
x=int(input("Enter the value of x: "))
e=2.718281
fact=1
for i in range(1,x+1):
  fact*=i
p=((l**x)*(e**(-l)))/fact
print("The probability is: {:.4f} ".format(p))
