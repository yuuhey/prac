import sys
lst = []
for _ in range(int(sys.stdin.readline())):
    lst.append(sys.stdin.readline())
lst.sort()
for i in lst:
    print(i)