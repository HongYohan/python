print('한국','Seoul',2021)

#sep옵션을 사용하면 공백대신 그 지정한 값이 대체한다
print('한국','Seoul',2021,sep='-')

#각문단은 서로 ;으로 구분한다, 다음 줄 출력
print('한국','Seoul'); print('한국','Seoul')

#end로 지정하면 각문단이 하나의 문단으로 나온다, 같은 줄 출력
print('한국','Seoul',end=' '); print('한국','Seoul',2021,sep='-')