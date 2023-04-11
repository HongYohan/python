num=int(input("소수 : "))
allnum=[]

for i in range(1,num+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        allnum.append(i)
print("1부터 {}번 까지의 소수 집합 : {}".format(num,allnum))