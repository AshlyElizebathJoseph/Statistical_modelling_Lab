import numpy as np
from scipy.stats.stats import pearsonr

hand=[17,15,19,17,21]
height=[150,154,169,172,175]
x=np.corrcoef(hand,height)
print("Correlation value: ")
print(x)
val=pearsonr(hand,height)
lst=list(val)
print("Pearson value",lst)
if lst[1]>0.05:
  print("WE RJECT Ho.As ", round(lst[1],5)," is greater than 0.05")
