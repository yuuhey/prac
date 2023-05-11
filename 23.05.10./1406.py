from sys import stdin
input = stdin.readline

# abcd 0~4 0~5
s = input().rstrip()
loc = len(s)
for i in range(int(input())):
    c = list(input().split())
    if len(c) != 1:
        s = ''.join((s[:loc],c[1],s[loc:]))
        loc += 1
    else:
        if c[0] == 'L' and loc != 0:
            loc -= 1
        elif c[0] == 'D' and loc != len(s)+1:
            loc += 1
        elif c[0] == 'B' and loc != 0:
            s = ''.join((s[:loc-1], s[loc:]))
            loc -= 1
print(s)
