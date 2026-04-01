#Infinite Even num generator -Generators
def even_gen():
    n=2
    while True:
        yield n
        n+=2
g=even_gen()
for i in range(5):
    print(next(g))