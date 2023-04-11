name="홍요한" #문자열
givename=name[1:3]
print(name[0])
print(givename)
print(name*30)


city=['서울시',200,'부산시',400] #리스트
print(city[-2])
print(city[2:])
city[2]='부산광역시'
print(city[2])
print('서울시' in city)

a=(1,2,3,4,5) #튜플
print(a[1:4])
print(a[::2])
print(a[-10:10])
print(len(a))