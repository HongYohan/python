num=int(input("사용자 입력 : "))
i=0
hap=0
count=0

while True:
    i=i+1
    if i%3==0:
        hap=hap+i
        count=count+1
        if hap >num:
            print("{}을 넘었을 때의 값 : {}".format(num,i))
            print("{}을 넘었을 때까지의 합 : {}".format(num,hap))
            print("{}을 넘었을 때까지 몇 번째 3의 배수인가 : {}".format(num,count))
            break
