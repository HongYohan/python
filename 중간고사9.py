kg=float(input('몸무게를 kg 단위로 입력하세요 : '))
m=float(input('키를 미터 단위로 입력하세요 : '))

bmi=kg / (m**2)
bmi=round(bmi,2)

print('당신의 BMI = {}'.format(bmi))