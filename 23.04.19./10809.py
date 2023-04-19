import string

s = input().lower()

alpha = [*string.ascii_lowercase]

for i in alpha:
    if i in s:
        print(s.find(i), end = " ")
    else:
        print("-1", end = " ")