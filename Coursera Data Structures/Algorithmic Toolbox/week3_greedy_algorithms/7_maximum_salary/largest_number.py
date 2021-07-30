n = int(input())
digits = list(map(int,input().split()))

def Find(digits):
    output = [] #empty array 
    while len(digits) !=0:
        maxdigit = -4
        for digit in digits:
            D1 = str(digit)
            D2 = str(maxdigit)
            if D1[0]>D2[0]:
                maxdigit = digit
            elif D1[0] == D2[0]:
                if len(D1) == 1 and D2[1] <D2[0]:
                    maxdigit = digit
                    continue
                if len(D1) == 1 and D2[1] > D2[0]:
                    continue
                if D1[1] >D1[0] and len(D2) == 1:
                    maxdigit = digit
                if len(D2[1]) == 1 and D1[1] < D1[0]:
                    continue
    #now starting algorithm for 3 digit numbers
                if D1[1] >D2[1]:
                    maxdigit = digit 
                elif D1[1] == D2[1]:
                    if len(D1) == 2 and D2[2] <D2[1]:
                        maxdigit = digit
                        continue
                    if len(D1) == 2 and D2[2] > D2[1]:
                        continue
                    if D1[2] >D1[1] and len(D2) == 2:
                        maxdigit = digit
                    if len(D2[1]) == 2 and D1[2] < D1[1]:
                        continue
                    if D1[2] > D2[2]:
                        maxdigit = digit

        output.append(maxdigit)
        digits.remove(maxdigit)
    return output

value = Find(digits)
print(*value,sep = '')                   
