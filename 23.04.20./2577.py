mul = 1
for _ in range(3):
    mul *= int(input())
mul = str(mul)
for i in range(10):
    print(mul.count(str(i)))