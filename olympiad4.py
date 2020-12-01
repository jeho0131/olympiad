#7명의 면접을 보는데 각각 점수를 매긴다. 가장 큰점수와 가장 작은 점수를 제외하고
#나머지 5명의 점수의 평균을 소수점 3번째자리에서 반올림해 출력한다.
p = []
p = input().split()
intp = list(map(int,p))

big = 0
small = 0
add = 0

for i in range(0,len(intp)):
    if intp[big] < intp[i]:
        big = i
    elif intp[i] < intp[small]:
        small = i

for j in range(0,len(intp)):
    add += intp[j]
add = add - intp[big] - intp[small]
add = add / 5

print('%.2f' % add)
