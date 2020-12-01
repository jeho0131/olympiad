s = int(input())
num = input().split()
intnum = list(map(int,num))
rank = [1 for i in range(0, 1000)]

for i in range(0, s):
    for j in range(0,s):
        if intnum[i] < intnum[j]:
            rank[i] += 1

for k in range(0,s):
    print(intnum[k], rank[k],"\n")

            
