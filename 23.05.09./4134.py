from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    while True:
        breaker = False
        for i in range(2,n//2+1):
            if n%i==0:
                breaker = True
                break
        if breaker==False:
            print(n)
            break
        n+=1
