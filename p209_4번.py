num=eval(input("최초의 리스트 : "))

turn=int(input("회전 횟수 : "))

i=0
while i <turn:
    if type(num) == list:
        num.insert(0,num[len(num)-1])
        del num[len(num)-1]
        
    i=i+1



print(num)