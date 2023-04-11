tax=int(input('자동차 세금 : '))
addtax=float(input('부과된 가산금(소수점자리로 표시) : '))
total=tax+(tax*addtax)
print("최종 자동차 세금 : {}".format(int(total)))