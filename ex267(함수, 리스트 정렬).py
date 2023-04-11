def sort_Insertion(subnum):
    for i in range(1,len(subnum)):
        for j in range(i,0,-1):
            if subnum[j]>subnum[j-1]:
                temp=subnum[j]
                subnum[j]=subnum[j-1]
                subnum[j-1]=temp
            else:break
    return sum(subnum)

s= input("10개의 정수 스페이스로 입력 :")
string_list=s.split() # 스페이스 기준으로 리스트화
num_list=[]
for i in string_list: # 자동 오름차순 정렬
    num_list.append(int(i))
    
print("최초의 리스트 :",num_list)
hap=sort_Insertion(num_list)
print("내림차순 :",num_list)
print("리스트 합 :",hap)