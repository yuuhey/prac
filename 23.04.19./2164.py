from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

while len(queue)!=1:
    queue.popleft()
    queue.append(queue.popleft())

print(*queue)