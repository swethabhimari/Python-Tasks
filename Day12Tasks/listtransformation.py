data=[[1,2,3],[4,5],[6]]
flat_list=[item for sublist in data for item in sublist]
#square
even_sq=[x**2 for x in flat_list if x % 2 == 0]
print("Square of even numbers:",even_sq)
print(flat_list)

#one line
result=[x**2 for sublist in data for x in sublist if x%2==0]
print(result)