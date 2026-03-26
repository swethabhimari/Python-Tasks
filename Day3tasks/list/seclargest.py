#without sorting sorting
lst = [10, 20, 4, 45, 99]

first = second = float('-inf')

for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

if second == float('-inf'):
    print("No second largest number")
else:
    print("Second largest number:", second)