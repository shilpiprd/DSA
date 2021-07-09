n,W = map(int,input().split())
diction = {}
count = 0
for _ in range(n):
	vi , wi = map(int,input().split())
	if wi == 0:
	    n -=1
	else:
	    diction[wi] = float(vi/wi)
listdic = list(diction.items()) 
listdic.sort(key = lambda x: x[1],reverse = True)  #gives list of tuples in decreasing order
for i in range(len(listdic)):
    if W == 0:
        break
    key = listdic[i][0]
    value = listdic[i][1]
    a = min(W,key)
    count += a * float(value)
    W -=a
print(format(count,'.4f'))  
