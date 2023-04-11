# with open("C:/Users/82106/Desktop/Python/txt/sales.txt","w") as f:
#     while True:
#         num1=input("테이블 번호를 입력하시오(1~5, 끝:0) : ")
#         if int(num1)==0:
#             print("영업이 종료되었습니다. 수고하셨습니다.")
#             break;
#         count1=input("그릇 수를 입력하시오 : ")
#         f.write(num1+' ')
#         f.write(count1+'\n')



from dataclasses import field


with open("C:/Users/82106/Desktop/Python/txt/sales.txt","r") as f:
    txts= f.read()
    txts=txts.split()

with open("C:/Users/82106/Desktop/Python/txt/total_sales.txt","w") as f:
    i=0
    price=0
    all=0
    while True:
        if i %2==1:
            price=7500*int(txts[i])
            all=all+price
            print(txts[i-1],"번 테이블 매출 :",price,file=f)
        i=i+1
        if i == len(txts):
            print("오늘의 총 매출 :",all, file=f)
            break;