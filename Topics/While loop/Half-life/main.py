count = 0
initial = int(input())
final = int(input())
while initial > final:
    initial //= 2
    count += 1
if initial < final:
    print(count*12)
