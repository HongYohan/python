hap=0
cnt=0
avg=0
for i in range(1,11):
    num=int(input("{}번째 숫자 입력 : ".format(i)))
    
    if num>0:
        hap=hap+num
        cnt=cnt+1
        avg=hap/cnt
        if i==10:
            print("합 :",hap,"평균 :",avg)