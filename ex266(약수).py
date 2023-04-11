def findPrime(x,y):
    for i in range(1,x+1):
        if x%i==0:
            y.append(i)
    
num=int(input("자연수를 입력 : "))
lis=[]
findPrime(num,lis)
print(num,"의 약수는 :",lis)