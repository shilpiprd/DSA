
N = int(input())
L = list(map(int,input().split()))
L.sort()
if N == 1:
	print(L[0])
else:
	print(L[-1] * L[-2])
