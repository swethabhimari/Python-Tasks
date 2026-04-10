import copy
classes=[["Math",[30,35]],
         ["Science",[25,28]]]
deep_copy=copy.deepcopy(classes)
#modify original data
classes[0][1][0]=45
print("original data changes:",classes)
print("copied data",deep_copy)
print("Nested lists inside lists where deep copy completely creates separate copy " \
"so modifying original data will not effect the copied data.")