#Secure login system(Decorators)
#logged_in=False
logged_in=True
def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Please login first")
    return wrapper
@login_required
def dashboard():
    print("Welcome to dashboard")
dashboard()