t = (10, 20, 30)
lst = list(t)

lst[1] = 99  # modify element

t = tuple(lst)
print("Modified tuple:", t)