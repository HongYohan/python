salary=int(input('이번달 본봉 : '))
bonus=int(input('이번달 보너스 : '))
total=salary+bonus
altax=float(input('이번달 세금 : '))
tax=total*altax
money=total-tax

print("홍길동의 이번달 본봉은 {0}이고 \
보너스는 {1}이므로 총 금액은 : {2} 여기서 세금은 {3}이다".format(salary, bonus, money, altax))