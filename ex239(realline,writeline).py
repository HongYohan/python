L1=['충청남도','충청북도\n','전라남도','전라북도\n','경상남도','경상북도\n\n']

with open("C:/Users/82106/Documents/LineTest.txt","w") as f :
    f.writelines(L1) #리스트 내용 문자열 저장

with open("C:/Users/82106/Documents/LineTest.txt","r") as f :
    for line in f :
        print(line,end='') #줄바꿈을 하지않고 연속으로 출력
        
with open("C:/Users/82106/Documents/LineTest.txt","r") as f :
    while True:
        line=f.readline()
        print(line,end='')  #줄바꿈을 하지않고 연속으로 출력
        if line =='':       #리스트 요소가 비어있으면 반복문을 벗어남
            break
        
with open("C:/Users/82106/Documents/LineTest.txt","r") as f :
    textLists = f.readlines() #파일에 있는 모든 줄을 하나의 리스트 항목으로 반환
    print(type(textLists)) 
    print(textLists)

with open("C:/Users/82106/Documents/LineTest.txt","r") as f :
    textLists=f.readlines()
    for line in range(len(textLists)) : #in textLists를 range로 바꿈
        print(textLists[line],end='')
        
f = open("C:/Users/82106/Documents/ptest.txt","w")

print("aaaaaaaa",file=f) #file 매개변수를 이용해 파일객체를 지정하여 파일에 출력
print("bbbbbbbb",file=f)
print("cccccccc",file=f)

f.close()