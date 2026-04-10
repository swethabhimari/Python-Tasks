import numpy as np
#float val 0to1
value=np.random.rand(8)
#normalize
normalized=value*100
#filter val>50
filtered=normalized[normalized>50]
#sort
sorted=np.sort(filtered)
print("Normalized:",normalized)
print("Filtered(>50):",filtered)
print("sorted:",sorted)