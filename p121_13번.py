dish=int(input('음식 값 : '))
tax=float(input('부가세(소숫점자리로 표시) : '))
altax=dish*tax
total=dish+altax
print("총 식사 금액 : {}".format(int(total)))