x, num = map(int,input().split())
ax = 0
bx = 0
cake = [ [0] * 3 ] * num
cakeup = [0 for i in range(x)]

for i in range(0, num):
    cake[i] = list(map(int,input().split()))

for j in range(0, num):
    ax = cake[j][0]
    bx = cake[j][1]
    for k in range(ax-1, bx):
        cakeup[k] += cake[j][2]

for p in range(0, x):
    print(cakeup[p], end='')
