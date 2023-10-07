from collections import deque
 
N, L = map(int, input().split())
A = list(map(int, input().split()))
 
D = [] 
deque = deque() 
 
for i in range(N):
    while deque and deque[0] < i - L + 1:
        deque.popleft()
 
    while deque and A[deque[-1]] > A[i]:
        deque.pop()
 
    deque.append(i)
    D.append(A[deque[0]])
 
print("")
print(*D)
