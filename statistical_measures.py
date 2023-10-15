import statistics as st
import numpy as np
import matplotlib.pyplot as plt

data=[1,2,3,4,5,4,9,4]
print("Mean: ",st.mean(data))
print("Median: ",st.median(data))
print("Mode: ",st.mode(data))
print("Standard Deviation: ",np.std(data))
print("Percentile: ",np.percentile(data,50))

x=np.linspace(1,50,200)
mean=np.mean(x)
sd=np.std(x)
prob_density=(np.pi*sd)*np.exp(-0.5*((x-mean)/sd)**2)
plt.plot(x,prob_density)
plt.title("Normal Distribution")
plt.show()
