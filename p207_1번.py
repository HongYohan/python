str=input("문자열을 입력 : ")
str=str.strip()
str=str.upper()
list1=[]
list2=[]
list1.extend(str)
list2.extend(str)
list2.reverse()
for i in range(len(list1)):
    if ' ' in list1 and ' ' in list2:
        list1.remove(' ')
        list2.remove(' ')


# print(list1,list2)

if list1==list2:
    print("회문입니다")
else:
    print("회문이 아닙니다")