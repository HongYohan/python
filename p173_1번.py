a=0
while True:
    hap=0
    avg=0
    cnt=0
    for i in range (1,4):
        num=int(input("성적 입력 : "))
    
 
        hap=hap+num;
        cnt=cnt+1
        if cnt %3==0:
            a=a+1
            avg=hap/3
            print("총점 {}점, 평균 {}점".format(hap,avg))

    if cnt==3 and hap ==0:
        print("총 {}명의 성적 처리".format(a-1))
        break;