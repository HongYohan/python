num1=int(input("숫자1 입력 : "))
num2=int(input("숫자2 입력 : "))
exnum=0
total=0
if num1 >num2 :
    exnum=num1
    num1=num2
    num2=exnum

for i in range(num1,num2+1):
    if i%2==0 and i%3!=0:
        total=total+i
        print(i,end=' ')
print('\n{}부터 {}까지의 합 :{}'.format(num1,num2,total))