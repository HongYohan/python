num=[]
count=0
for i in range(1,1001):
    cnt=0
    for j in range(1,i+1):
        
        if i%j == 0:
            cnt=cnt+1
    if cnt==2:
        num.append(i)
        count=count+1



print(num, count)