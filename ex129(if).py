# score = int(input('총점 입력 : '))

# if (score>=80) : #콜론 필수
#     print('합격!!!')
#     print('축하합니다.')

# print('프로그램 종료')


korean= int(input('국어 성적 입력 : '))
english= int(input('영어 성적 입력 : '))
math= int(input('수학 성적 입력 : '))
total= korean+english+math
average= total/3
average=round(average,2)

if (average >= 90):
    print('당신의 평균은 {}점 입니다.'.format(average))
    print('축하합니다. A+입니다.')

print('감사합니다.')