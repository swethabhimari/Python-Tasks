def check_even_odd(n):
    if n % 2==0:
        return "Even"
    else:
        return "odd"
num=int(input("Enter a number:"))
print(check_even_odd(num))