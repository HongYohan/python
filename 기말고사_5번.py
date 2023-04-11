f=open("C:/Users/82106/Desktop/jumsu.txt","w")
f.close()

with open("C:/Users/82106/Desktop/jumsu.txt","r") as f:
    jumsu=f.readlines()
    # for i in range(0,len(jumsu)-1):
    #     jumsu[i]=jumsu[i][0]+jumsu[i][1]
    # 어떻게 하면 jumsu라는 리스트의 각 문자 요소를 정수로 바꿀수 있을까?


with open("C:/Users/82106/Desktop/result.txt","w") as f:
    print("전체 합 :",sum(jumsu),file=f)
    print("전체 합 :",sum(jumsu)/len(jumsu),file=f)