n = int(input())
L =[]
for _  in range(n):
    #take input of segments and append it as tuples
    a,b = map(int,input().split())
    L.append((a,b))

L.sort(key = lambda x:x[1])
# L = [(1, 3), (2,5), (5, 6),(4,7)] 
point = L[0][1] 
req_set = dict()
req_set[point] = 0

for i in L[1:]:
    if i[0] <= point:
        req_set[point] =  req_set.get(point,0) +1
    else:
        point = i[1]
        req_set[i[1]] = req_set.get(i[1],0) + 1

print(len(req_set))
print(*list(req_set.keys()))
