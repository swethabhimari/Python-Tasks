#Word counter program
#first write content into the file
with open("article.txt","w") as f:
    text=input("Enter your article:\n")
    f.write(text)
#Read content from file
with open("article.txt","r") as f:
    content=f.read()
#count words ,lines,characters
words=content.split()
lines=content.split("\n")
characters=len(content)

#display results
print("\nResults:")
print("Words:",len(words))
print("Lines",len(lines))
print("Characters",characters)