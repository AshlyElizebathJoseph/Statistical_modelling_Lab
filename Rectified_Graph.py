import matplotlib.pyplot as plt
import numpy as np

plt.figure()
pi=np.pi
x=np.linspace(0,2*pi,1000)
y=np.sin(x)
z=abs(y)
plt.plot(x,y)
plt.plot(x,z)
plt.show()

plt.figure()
plt.plot(x,y)
plt.title("INPUT")
plt.show()
plt.figure()
plt.plot(x,z)
plt.title("OUTPUT")
plt.show()
