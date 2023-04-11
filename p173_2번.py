num1= int(input("첫 번째 수 : "))
num2= int(input("두 번째 수 : "))

if num2<num1:
    temp=num2
    num2=num1
    num1=temp

hap=0
i=0
for i in range(num1,num2+1):
    if i%2 ==1:
        hap=hap+i
    i=i+1

print("{}와 {} 사이 홀수의 합 : {}".format(num1,num2,hap))