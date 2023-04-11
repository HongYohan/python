from numpy import sort


num=int(input("숫자를 입력하시오 : "))


mul2=set()
mul3=set()
mul7=set()
multi=set()
for i in range(1,num):
    if i%2==0:
        mul2.add(i)
    if i%3==0:
        mul3.add(i)
    if i%7==0:
        mul7.add(i)
    if i%2==0 and i%3==0 and i%7==0:
        multi.add(i)
print("2의 배수 :",mul2)
print("3의 배수 :",mul3)
print("7의 배수 :",sorted(mul7))
print("2,3,7의 배수 :",multi)