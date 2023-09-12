def longestSequence(a, s, n):
    max_len=1
    i=0
    while i<n:
        left=a[i]-1
        right=a[i]+1
        count=1
        while left in s :
            count+=1
            s.remove(left)
            left+=1
        while right in s :
            count+=1
            s.remove(right)
            right+=1
        max_len=max(max_len,count)
        i+=1
    return max_len

import random
N = int(input('난수의 개수 : '))
while N < 1:
    print('난수의 개수는 자연수여야 합니다.')
    N = int(input('난수의 개수 : '))
A = []
for i in range(N):
    A.append(random.randint(1, N))
print('리스트 : ', A)
S = set(A)
print('집합 : ', S)        
print('최장 연속 순차의 길이 : ', longestSequence(A, S, N))
