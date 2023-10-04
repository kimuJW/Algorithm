N, M = map(int, input().split())
A = list(map(int, input().split()))
 
pre_sum = [0]
count = {0: 1}
result = 0
 
for num in A:
    pre_sum.append((pre_sum[-1] + num) % M)
    rest = pre_sum[-1]
    
    if rest in count:
        result += count[rest]
        count[rest] += 1
    else:
        count[rest] = 1
 
print('')
print(result)
