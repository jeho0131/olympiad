def add(num):
    n = []
    p = 0
    plus = 0
    
    if len(num) == 1:
        return num
    
    else:
        n = list(map(int,num))
        
        for j in range(0, len(num)):
            p += n[j]

        p = str(p)
        plus = add(p)
        return plus

num = input()
plus = add(num)

print(plus)
    
    
