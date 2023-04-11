# while True:
#     dan=int(input("단 입력 : "))
#     if (dan>=2 and dan<=9):
#         for i in range(1,10):
#             print('{}*{}={}'.format(dan,i,dan*i))
#     else :
#         break;



num=int(input("소수 검증 숫자 입력 : "))
for i in range(2,num):
    if(num%i == 0):
        print("소수가 아닙니다.")
        break
    
    else:
        print("소수")
        break;