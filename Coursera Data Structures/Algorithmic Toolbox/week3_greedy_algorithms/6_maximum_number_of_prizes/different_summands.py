n = int(input())
i = 1
L =[]

while n !=0:
    n -=i
    if n -(i+1) <0:
        n+=i
        i = n
        n-=i
        L.append(i)
        continue
    L.append(i)
    i+=1

print(len(L))
print(*L)
