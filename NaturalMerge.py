def merge(a, l, m, r):
    i = l
    j = m + 1
    k = l
    
    while i <= m and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            i = i + 1
        else:
            b[k] = a[j]
            j = j + 1
            
        k = k + 1
 
    if m < i:
        while j <= r:
            b[k] = a[j]
            k = k + 1
            j = j + 1
    else:
        while i <= m:
            b[k] = a[i]
            k = k + 1
            i = i + 1
 
    for t in range(l, r+1):
        a[t] = b[t]
  
def makeRun(a, n): 
    r = []
    r.append(0)
    for i in range(1, n):
        if a[i] > a[i+1]:
            r.append(i)
    r.append(n)
    while len(r)  > 2:
        new_r = [0]
        for i in range(0, len(r)-2, 2):
            merge(a, r[i]+1, r[i+1], r[i+2])
            new_r.append(r[i+2])
        if len(r)%2 == 0:
            new_r.append(r[-1])
        r = new_r
   
def checkSort(a, n):
    isSorted = True
 
    for i in range(1, n):
        if a[i] > a[i+1]:
            isSorted = False
            
        if not isSorted:
            break
 
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")
 
import random,time
 
N = 10000
a = []
a.append(-1)
 
for i in range(N):
    a.append(random.randint(1, N))
 
b = a.copy()
 
start_time = time.time()
 
makeRun(a, N)
 
end_time = time.time() - start_time

print("자연 합병 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))
checkSort(a,N)