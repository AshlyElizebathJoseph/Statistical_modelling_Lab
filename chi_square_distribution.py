females=[60,54,46,41]
males=[40,44,53,57]
total=[100,98,99,95]
f_exp=[]
m_exp=[]
r=0
for i in total:
  f_exp=((i*201)/395)
  f_exp.append(f_exp1)
for j in total:
  m_exp=((j*194)/395)
  m_exp.append(m_exp1)
print("Expected value of Females: ",f_exp)
print("Expected value of Males: ",m_exp)
gender=females+males
print("Gender: ",gender)
exp=f_exp+m_exp
print("Expected Value: ",exp)
for i,j in zip(gender,exp):
  r=r+((i-j)**2/j)
print("Result: ",r)
import scipy.stats as stats
stats.chisquare(gender,exp)
lst=list(res)
print(res)
if lst[1]>0.05:
  print("We accept null hypothesis,since ",round(lst[1],5)," is greater than 0.05)

