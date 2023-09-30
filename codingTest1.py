N, M = map(int, input().split())  

print()  

  

a = []  

  

for _ in range(N):  

    b = list(map(int, input().split()))  

    a.append(b)      

  

def sum(a,x1,x2,y1,y2):  

    sum=0  

    for i in range (x1, y1+1):  

        for j in range(x2,y2+1):  

            sum+=a[i-1][j-1]  

    return sum  

  

result=[] 

  

for _ in range(M):  

    b=list(map(int, input().split()))  

    result.append(sum(a,b[0],b[1],b[2],b[3]))  

     

print('\n') 

  

for i in result:  

    print(i) 