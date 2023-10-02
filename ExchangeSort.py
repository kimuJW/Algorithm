def exchangeSort(a, n):
    for i in range(1, n):
        for j in range(i+1, n+1):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
        
def checkSort(a, n):
    isSorted = True
 
    for i in range(1, n):
        if a[i] < a[i+1]:
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
 
exchangeSort(a, N)
 
end_time = time.time() - start_time
 
print("교환 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))
checkSort(a,N)