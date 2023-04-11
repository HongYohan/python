import random

num=[]
while True:
    if len(num)<10:
        num.append(random.randint(1,100))
    if len(num) ==10:
        break;
print("생성된 리스트 :",num)
list=[1,2,3]
num1=[]
num2=[]
num3=[]
for i in range(0,10):
    if num[i]<10:
        num1.append(num[i])
    elif num[i]>=10 and num[i]<100:
        num2.append(num[i])
    else:
        num3.append(num[i])
last=[]
last.append(num1)
last.append(num2)
last.append(num3)
dict=dict(zip(list,last))

print("생성된 사전 :",dict)