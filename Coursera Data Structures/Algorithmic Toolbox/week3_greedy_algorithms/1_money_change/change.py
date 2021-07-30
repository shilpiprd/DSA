n = int(input())
count = 0
rem = n % 10
count += n // 10
if rem!=0:
    count+=rem //5
    rem = rem % 5
if rem !=0:
    count += rem
print(count)
