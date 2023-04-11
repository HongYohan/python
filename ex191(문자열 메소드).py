st=input("영어 문장을 입력 : ")

print("입력된 문장의 길이는 : ",len(st))

print("각 단어의 첫 문자를 대문자로 변환 : ",st.title())

print("모든 글자를 대문자로 변환 : ",st.upper())

print("문자열에 a가 몇번 나타났는가 : ",st.count("a"))

print("입력된 문자열의 모두 문자로만 구성되었는가? : ",st.isalpha())

print("입력된 문자열이 모두 숫자로만 구성되었는가? : ",st.isdigit())

print("입력된 문자열이 모두 대문자 구성되었는가? : ",(st.upper()).isupper())

print("문장에서 스페이스 개수 : ",st.count(' '))

print("스페이스가 삭제된 문장 : ", st.replace(' ', ''))

print("스페이스로 문자열 분리 : ",st.split(" ")) # 리스트로 반환
# splitlines() \n기준으로 분리하여 리스트로 반환

st.partition('Python') #python을 기준으로 3개 나눠 튜플로 반환