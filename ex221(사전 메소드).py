list1=[2019111,2019112,2019113]
list2=[99,98,97]
dict1=dict(zip(list1,list2)) #zip을 이용해 2개의 리스트를 합치고 dict로 사전을 만듬
print(dict1)
for i in dict1:
    print(dict1[i]) #키값을 기준으로 반복처리
    
dict1.get(99) # dict1의 99번 키 값을 가져옴
dict2=dict1.copy() # 사전복사
dict2.clear()   #사전의 모든 요소 삭제

dict2={2019114:96, 2019115:95}
dict1.update(dict2)
print(dict1)