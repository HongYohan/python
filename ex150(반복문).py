# i=1
# while i<=5:
#     name=input("이름을 입력하세요 : ")
#     print(name+"씨 환영합니다")
#     i=i+1
    
    
# i=0
# while i<100:
#     name=input("이름을 입력하세요 : ")
#     print(i+1,"번",name+"씨 환영합니다")
#     i=i+1


# i=1
# while i<=100:
#     if i%2 != 1 : #짝수 조건
#         name=input("이름을 입력하세요 : ")
#         print(i,"번",name+"씨 환영합니다")
#     i=i+1


# i=1
# hap=0
# while i<=1000:
#     hap=hap+i
#     i=i+1
# print('{}번째 합 : {}'.format(i-1,hap))


# end=int(input("합계를 원하는 숫자 입력 : "))
# start=int(input("시작값을 입력하시오 : "))
# i=start
# hap=0
# while i <= end:
#     hap=hap+i
#     i=i+1
# print('{}부터 {}까지의 합 : {}'.format(start, end, hap))


# start=int(input("시작값 : "))
# end=int(input("끝 값 : "))
# i=start
# hap=0
# hap1=0
# while i <= end:
#     if i%2 == 0:
#         hap=hap+i
#     else:
#         hap1=hap1+i
#     i=i+1
# print('{}부터 {}까지의 짝수의 합 : {}'.format(start, end, hap))
# print('{}부터 {}까지의 홀수의 합 : {}'.format(start, end, hap1))


# start=int(input("시작값 : "))
# end=int(input("끝 값 : "))
# i=start
# hap=0
# hap1=0
# if i <= end:
#     while i <= end:
#         if i%2 == 0:
#             hap=hap+i
#         else:
#             hap1=hap1+i
#         i=i+1
#     print('{}부터 {}까지의 짝수의 합 : {}'.format(start, end, hap))
#     print('{}부터 {}까지의 홀수의 합 : {}'.format(start, end, hap1))
# else:
#     while i >= end:
#         if end%2 != 1:
#             hap=hap+end
#         else:
#             hap1=hap1+end
#         end=end+1
#     print('{}부터 {}까지의 짝수의 합 : {}'.format(end, start, hap))
#     print('{}부터 {}까지의 홀수의 합 : {}'.format(end, start, hap1))


start=int(input("시작값 : "))
end=int(input("끝 값 : "))
if start > end :
    temp=start
    start=end
    end=temp

i=start
hap=0
hap1=0
if i <= end:
    while i <= end:
        if i%2 == 0:
            hap=hap+i
        else:
            hap1=hap1+i
        i=i+1
    print('{}부터 {}까지의 짝수의 합 : {}'.format(start, end, hap))
    print('{}부터 {}까지의 홀수의 합 : {}'.format(start, end, hap1))