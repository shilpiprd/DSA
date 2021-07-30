def minRefills(array,n,L):
    count = 0        #refers to the number of refils made
    currentRefil = 0 #refers to the n'th stop
    lastRefil = 0
    if L>array[-1]:
        return 0       
    while currentRefil <= n:
        lastRefil = currentRefil 
        while currentRefil <= n and array[currentRefil +1 ] - array[lastRefil] <=L:
            currentRefil +=1

        if currentRefil == lastRefil:
            return -1
        if currentRefil <=n:
            count+=1
    return count
        
finaldist = int(input())
arrayx = []
L = int(input())
n = int(input()) #gives no of stops in the middle
arrayx = list(map(int,input().split()))
arrayx.insert(0,0)
arrayx.append(finaldist) #now arrayx has n+1 elements
output = minRefills(arrayx,n,L)
print(output)

