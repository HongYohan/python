id=input('아이디를 입력하세요 : ')
pw=input('비밀번호를 입력하세요 : ')

if (id == 'admin' and pw == 'pw1234') :
    print('로그인 성공~')
    
else:
    print('아이디 혹은 비밀번호가 틀려요~')
    print('바르게 입력해주세요!')