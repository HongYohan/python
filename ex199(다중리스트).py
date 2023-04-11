list1=[[11,33,22,7],[77,2,90],[3,66,44,9,8]]

minvalue=min(list1[0])
maxvalue=max(list1[0])
allsum=0

for i in range(len(list1)) :
    print((i+1),"번째 줄의 합은 :", sum(list1[i]))
    allsum=allsum+sum(list1[i])
    
    
    if minvalue>min(list1[i]):
        minvalue=min(list1[i])
    if maxvalue<max(list1[i]):
        maxvalue=max(list1[i])
        
print("리스트에서 가장 작은 값은 : ",minvalue)
print("리스트에서 가장 큰 값은 : ",maxvalue)
print("리스트의 전체 합 : ",allsum)