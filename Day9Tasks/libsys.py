#Library management sys-constructor and inheritance
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
class Ebook(Book):
    def __init__(self, title, author,size):
        Book.__init__(self,title, author)
        self.size=size
    def display(self):
        print(self.title,self.author,self.size)
eb=Ebook("Python","Guido Van Rossum","5MB")
eb.display()
        