#Random Number Generator
def generator(n):
    for i in range(1,n+1):
        yield i
for num in generator(5):
    print(num)