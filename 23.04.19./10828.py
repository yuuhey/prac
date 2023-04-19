# 제출한 코드는 되는데 왜 이거는 런타임에러날까.. 아무리 봐도 똑같은거 같은데

import sys
n=int(sys.stdin.readline())

stack =[]
for _ in range(n):
    lst = sys.stdin.readline().split()
    if lst[0]=="push":
        stack.append(lst[1])
    elif lst[0]=="pop":
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif lst[0]=="size":
        print(len(stack))
    elif lst[0]=="empty":
        if len(stack)==0:
            print(1)
        else: print(0)
    elif lst[0]=="top":
        if len(stack) != 0:
            print(stack[1])
        else: print(-1)