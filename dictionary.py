dic = {'김용준' : 28, '하현수' : 30}
print(dic['하현수'])

# 딕셔너리 데이터 업데이트
dic['김용준'] = 27
print(dic['김용준'])

dic_2 = {'김용준': [25, 180, 72, '01040426418'], '최아진': [20]}
print(dic_2['김용준'][1],)

dic_3 = {'김용준': {'나이': 25, '키': 180, '몸무게': 72, '연락처': '010-454-454'}}
print(dic_3['김용준'])