import random

def toss(lim):
  num=res=0
  for i in range(0,lim):
    res=random.randint(0,1)
    print(res)
    if (res==1):
      num+=1
    prob=num/lim
    print("Number of Heads occured: ",num, "\n Probability: ",prob)

choice=int(input("Enter number of tosses: "))
toss(choice)
