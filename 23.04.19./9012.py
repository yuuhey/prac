n = int(input())
def VPS(s):
    stack = []
    for i in s:
        if i=="(":
            stack.append(i)
        elif i==")":
            if len(stack)>0 and stack[-1]=="(":
                stack.pop()
            else:
                return "NO"
        else:
            continue
    if len(stack)==0:
        return "YES"
    return "NO"

for _ in range(n):
    print(VPS(str(input())))