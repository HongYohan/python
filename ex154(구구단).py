# i=1
# hap=0
# while True:
#     hap=hap+i
#     if i==100:
#         break
#     i=i+1
# print("hap=", hap)



while True:
    dan=int(input("몇 단 : "))
    i=1

    if dan<10 and dan>1:
        while i<10:
            print("{} * {} = {}".format(dan,i,dan*i))
            i=i+1
            
    else :
        print("2~9사이의 숫자를 입력하시오")
        break