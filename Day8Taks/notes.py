#create and write notes first
with open("notes.txt","w") as f:
    f.write("PYTHON file handling functions.")
 
# now Notes Reader Program
with open("notes.txt","r") as f:
    content = f.read()

print("Notes content:\n")
print(content)