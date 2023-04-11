num=int(input("숫자 입력 : "))

for i in range(num,0,-1):#for문 감소
    print(i,end='')
    for i in range(1,i+1): #for문 증가
        print("*",end='')
    print()
    i=i-1