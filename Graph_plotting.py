import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
ans=[]
for i in x:
  y=(i**4)+5
  ans.append(y)

print("Input values: ",x,"\n Claculated Values:", ans)
plt.plot(ans)
plt.title("Normal Distribution")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.show()
