text = ["A","B","C",'D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
text1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def passwordChange(t, m):
    n = 0
    for i in range(0,26):
        if t == text1[i]:
            n = (i + m) % 26
            t = text1[n]
            #break
            return t
    for j in range(0, 10):
        if t == num[j]:
            n = (j + m) % 10
            t = num[n]
            #break
            return t

move = int(input("이동시킬 문자수를 입력하시오 : "))
language = input("암호로 바꿀 문서를 입력하시오 : ")

for i in range(0,len(language)) :
    password = passwordChange(language[i], move)
    print(password, end='');
