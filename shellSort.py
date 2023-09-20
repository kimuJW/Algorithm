def shellSort(a, n):
    h = 1
    while h < n:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, n + 1):
            j = i
            v = a[i]
            while j > h and a[j - h] > v:
                a[j] = a[j - h]
                j -= h
            a[j] = v
        h //= 3

def checkSort(a, n):  
    isSorted = True  
    for i in range(1, n):  
        if (a[i] > a[i+1]):  
            isSorted = False  
        if (not isSorted):  
            break  
    if isSorted:  
        print("정렬 완료")  
    else:  
        print("정렬 오류 발생")

import random, time

N = 10000
a = []
a.append(None)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
shellSort(a, N)
end_time = time.time() - start_time
print('쉘 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(a, N)