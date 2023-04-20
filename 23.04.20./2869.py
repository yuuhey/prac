A, B, V = map(int, input().split())
total, day = 0, 0
while total < V :
    day +=1
    total +=A
    if total >= V:
        break
    total -=B
print(day)