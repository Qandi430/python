# 딕셔너리 자료형

# 딕셔너리란
# Key-value 구조의 자료형

# 딕셔너리 생성
dic = {'name':'pey','phone':'01099993323','birth':'1118'}
print(dic)
a = {1:'hi'}
a = {'a':[1,2,3]}

#딕셔너리 추가 -> a[key] = value
a = {1:'a'}
a[2] = 'b'
a['name'] = 'Qandi'
print(a)

#딕셔너리 삭제 ->  del a[key]
del a['name'] 
print(a)

#딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey':10,'julliet':99}
print(grade['pey'])
print(grade['julliet'])

# 딕셔너리 만들 때 주의할 사항
# 딕셔너리에서 key는 고유 값
a = { 1: 'a',1 : 'b'}
print(a[1]) # a[1] = b
# key에 리스트는  쓸수 없지만 튜플은 쓸수 있다. key 는 변하지 않는 값
# a = {[1,2],'hi'} # list는 쓸수 없다
a = {(1,2),'hi'}

# 딕셔너리 관련 함수
# key 리스트 만들기(keys)
a = {
        'name':'pey'
        ,'phone':'01199993323'
        ,'birth':'1118'
    }
print(a.keys())
# 파이썬 2.7버전 까지는 a.keys() 함수를 호출할 때 반환 값으로 리스트를 돌려준다. 
# 리스트를 돌려주기 위해서는 메모리 낭비가 발생하는데 파이썬 3.0이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_keys객체를 돌려준다.
# dict_values,dict_items 역시 파이썬 3.0 이후 버전에서 추가된 것들
# 3.0이후 버전에서 반환 값으로 리스트가 필요한 경우 list(a.keys())를 사용하면된다.
# dict_keys,dict_values,dict_items 등은 리스트로 변환하지 않더라도 기본적인 반복(iterate)구문에서 실행할 수 있다.

# value 리스트 만들기(values)
print(a.values())

# key,value 쌍 얻기(items)
print(a.items())

# key,value 쌍 모두 지우기(clear)
a.clear()
print(a)

# key로 value 얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('time'))
# a['name']은 a.get('name')을 사용했을때와 동일한 결과 값을 돌려받는다
# 다만 a['nokey']처럼 존재하지 않는 키로 값을 가져오려고 할 경우 a['nokey']는 요류를 발생시키고
# a.get('nokey')는 None을 돌려준다는 차이가 있다.

# 딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해둔 디폴트 값을 대신 가져오게 하고 샆을 때에는 get(x,default)를 사용하면 편리하다
print(a.get('foo','bar'))


# 해당 key가 딕셔너리 안에 있는지 조사(in) true or false로 반환
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print('email' in a)