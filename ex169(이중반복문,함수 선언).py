# dan=2
# while dan<=9:
#     print("== {}단 ==".format(dan))
#     i=1
#     while i<=9:
#         print("{} * {} = {}".format(dan, i, dan*i))
#         i=i+1
#     dan=dan+1




def lines(a):
    i=1
    line=a
    while i <=a:
        j=a
        print("{}".format(line),end='')
        while j>=i:
            print("*",end='')
            j=j-1
        print()
        i=i+1
        line=line-1
       

num=int(input("숫자 입력 : "))
lines(num) 