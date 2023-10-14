import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
# For Normal Graph
plt.plot(x)
plt.title("Normal graph")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.show()
plt.figure()

# For Stem Graph
plt.stem(x)
plt.title("Stem graph")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
