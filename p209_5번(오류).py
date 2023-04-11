num=eval(input("최초의 튜플 : "))

list=[]

for i in range(len(num)):
    if num[i] not in list:
        list.append(num[i])
        if num.count(num[i]) == 1:
            continue;
        else :
            print(num[i],"의 중복된 개수 :",num.count(num[i]))
            del num[i]

print("중복이 제거된 리스트 :",list)