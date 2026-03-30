#check palindrome
num = int(input("Enter a number:"))
#condition
if str(num)== str(num)[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome.")
