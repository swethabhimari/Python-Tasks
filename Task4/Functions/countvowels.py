def count_vowels(s):
    count=0
    for ch in s:
        if ch.lower() in 'aeiouAEIOU':
            count+=1
    return count
msg=input("Enter a string:")
print("Vowels:",count_vowels(msg))
            