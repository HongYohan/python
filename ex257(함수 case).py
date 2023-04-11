# 매개변수 x 반환값 x
def hap1():
    num1=int(input('숫자 1 : '))
    num2=int(input('숫자 2 : '))
    print(num1,"+",num2,"=",num1+num2)
hap1()#함수호출

# 매개변수 o 반환값 x
def hap2(a,b):
    print(a,"+",b,"=",a+b)

num1=int(input('숫자 1 : '))
num2=int(input('숫자 2 : '))
hap2(num1,num2)#함수호출

# 매개변수 x 반환값 o
def hap3():
    num1=int(input('숫자 1 : '))
    num2=int(input('숫자 2 : '))
    return num1, num2, num1+num2
a,b,c=hap3()#함수호출
print(a,"+",b,"=",c)

# 매개변수 o 반환값 o
def hap4(a,b):
    return a+b
num1=int(input('숫자 1 : '))
num2=int(input('숫자 2 : '))
c=hap4(num1,num2)#함수호출
print(num1,"+",num2,"=",c)