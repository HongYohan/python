def calc_list(a):
    print("합계는 {}이며, 평균은 {}입니다.".format(sum(a),sum(a)/len(a)))
    
print("********************")
print("입력한 숫자 계산하기")
print("********************")

lis1=[]
while True :
    num=int(input("계산 할 숫자 입력(종료? 0) : "))
    if num==0:
        break;
    lis1.append(num)
    if num >100:
        print("숫자는 1~100까지 입력 가능함!")
        lis1.pop()
    
    
print("입력한 숫자들 :",lis1)
calc_list(lis1)