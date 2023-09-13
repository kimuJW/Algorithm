def binarySearch(a, key, left, right):
    if left <= right :
        mid = (left + right) // 2
        if key == a[mid] :
            return mid
        elif key < a[mid] :
            return binarySearch(a, key, left, mid-1)
        else:  
            return binarySearch(a, key, mid+1, right);
    else:
        return -1;

a=[1,2,3,4,5,6,7,8,9,10]
key=int(input('key : '))
left = int(input('left : '))
right = int(input('right : '))
result = binarySearch(a,key,left,right)

if result != -1:
    print("key의 위치:", result)
else:
    print("key를 찾을 수 없습니다.")