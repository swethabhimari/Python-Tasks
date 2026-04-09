import numpy as np
#copy
dataset=np.array([10,20,30,40])
d_copy=dataset.copy()
dataset[0]=50
print("copy doesnot changed:",d_copy)
print("original array:",dataset)


#view
d_view=dataset.view()
dataset[1]=60
print("view of original array after changes:",d_view)
print("view of original array",d_view)