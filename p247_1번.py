import random

# "C:/Users/82106/Desktop/Python/txt/nume.txt"
i=1
num=""

avg=[]
while i<=5:
    cnt=0
    for j in range(1,6):
        c=random.randint(1,100)
        cnt=cnt+c
        num =num+ str(c)+" "
    avg.append(cnt)
    num=num+"\n"
    i=i+1

with open("C:/Users/82106/Desktop/Python/txt/nume.txt","w") as f :
    f.writelines(num)
    
with open("C:/Users/82106/Desktop/Python/txt/avg.txt","w") as f :
    for x in range(0,5):
        print(((x+1),"번째 학생의 평균 : ",avg[x]/5), file=f)