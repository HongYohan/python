num= int(input("숫자를 입력 : "))
list=[]

for i in range(1,num+1):
    count=0
    for j in range(1,i+1):
        if i%j ==0:
            count=count+1 #약수의 개수가 2개면 소수라는 뜻
    if count==2:
        list.append(i)
    

print("1부터 {}까지의 소수의 리스트 : {}".format(num,list))
print("1부터 {}까지의 소수의 개수 : {}".format(num,len(list))) 