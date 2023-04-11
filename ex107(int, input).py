name=input('이름 입력 : ')
score1=int(input('국어 성적 입력 : '))
score2=int(input('수학 성적 입력 : ')) # int는 문자열을 정수로 변환
total=score1+score2
average=total/2
print('{0}의 총점 : {1} \
평균 : {2}'.format(name, total, average))


'''
#int('문자열',base) base는 진법을 지정이고 기본은 10진법
num1=int(input('당신의 숫자를 2진법으로 입력 : '),2)
num2=int(input('당신의 숫자를 8진법으로 입력 : '),8)
print(num1, num2)
'''