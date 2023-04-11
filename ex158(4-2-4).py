num=int(input("합을 원하는 배수 입력 : "))
hap=0
for i in range(1,1001):
    if i%13==0:
        hap=hap+i
    
    
print("1~1000까지 {} 배수의 합 : {}".format(num,hap))