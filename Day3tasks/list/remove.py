
lst = [1, 2, 2, 3, 4, 4, 5]
unique_lst = []

for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)

print("List after removing duplicates (order preserved):", unique_lst)