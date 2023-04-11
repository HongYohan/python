fruit=('사과','배','파인애플','포도')
price=(5000,7000,4500,6000)

list=[]

for i in range (len(fruit)):
    list.append(fruit[i])
    list.append(price[i])
    
print("과일 튜플 :",fruit)
print("가격 튜플 :",price)
print("튜플로부터 생성된 과일+가격 리스트 :",list)


# num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0,8)
# print("생성된 튜플 :",num)
# for i in range(len(num)):
#     if num.count(i) ==0:
#         break
#     print(i,"개수 :",num.count(i))

num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0)
print("생성된 튜플 :",num)

list=[]

for i in range(len(num)):
    if num[i] not in list:
        list.append(num[i])
        if num.count(num[i]) == 1:
            continue;
        else :
            print(num[i],"개수 :",num.count(num[i]))