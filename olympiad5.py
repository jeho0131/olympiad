n = int(input())
num = input().split()
intn = list(map(int,num))
s = 0

for i in range(0, n):
    if intn[i] % 2 == 0:
        s -= 1
    elif intn[i] % 3 == 0:
        s -= 1
    elif intn[i] % 5 == 0:
        s -= 1
    elif intn[i] % 7 == 0:
        s -= 1

print(s)
