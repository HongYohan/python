# age=int(input('나이 입력 : '))
# adult=age >= 18 and age <=25
# print('그/그녀는 성인인가? : {}'.format(adult))

age=int(input('나이 입력 : '))
sex=input('성별은 : ')
nam= sex=='male' and age >= 18 and age <=25
print('조건의 결과 {}'.format(nam))