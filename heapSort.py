def heapify(a, h, m):
    v = a[h]
    j = 2 * h

    while j <= m:
        if j < m and a[j] < a[j + 1]:
            j += 1
        if v >= a[j]:
            break
        a[h], a[j] = a[j], a[h]
        h = j
        j = 2 * h

def heapSort(a, n):
    for i in range(n // 2, 0, -1):
        heapify(a, i, n)

    for i in range(n, 0, -1):
        a[1], a[i] = a[i], a[1]
        heapify(a, 1, i - 1)

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

for i in range(N):  
    a.append(random.randint(1, N)) 
a.sort(reverse=True)
a.insert(0,None)  

start_time = time.time()
heapSort(a,N)
end_time = time.time() - start_time
print('히프 정렬의 실행 시간 (N = %d): %0.3f 초' % (N, end_time))
checkSort(a, N)