import random

num=set()
while True:
    if len(num)<10:
        num.add(random.randint(1,100))
    if len(num) == 10:
        break;

print("집합 :",num)
num=list(num)
for i in range(1,len(num)):
    for j in range(i,0,-1):
        if num[j] < num[j-1]:
            temp=num[j]
            num[j]=num[j-1]
            num[j-1]=temp
print("큰수 :",num[len(num)-1])
print("작은 수 :",num[0])