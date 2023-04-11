i=0
hap=0
while (i<10):
    i=i+1
    num=int(input("정수 입력 : "))
    if i %2 == 0:
        num=-num
    hap=hap+num

print("합 :",hap)