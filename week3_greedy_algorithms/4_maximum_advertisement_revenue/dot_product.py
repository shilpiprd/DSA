n = int(input())
Ai = list(map(int,input().split()))
Bi = list(map(int,input().split()))


Ai.sort()
Bi.sort()
maxprofit = 0
for i in range(n):
    maxprofit+=Ai[i] * Bi[i]

print(maxprofit)
