# 문자열
# 문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합을 의미

# 문자열 사용법
# 1. 큰따옴표(")로 양쪽 둘러싸기
# 2. 작은따옴표(')로 양쪽 둘러싸기
# 3. 큰따옴표(""") 3개로 양쪽 둘러싸기
# 3. 작은따옴표(''') 3개로 양쪽 둘러싸기

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
# 변수에 저장
food = "Pythons's favorite food is perl"
print(food)
say = '"Python is very easy." he says.'
print(say)
# 백슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
print(food)
say = "\"Python is very easy.\" he says."
print(say)

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 이스케이프코드 \n 삽입
multiline = "Life is too short\nYou need python"
print(multiline)
# 연속된 작은따옴표 또는 큰따옴표 3개 사용하기
multiline = '''
Life is Too short
You need python
'''
print(multiline)


# 문자연산
head = "Python"
tail = " is fun"
print("head : ",head,", tail :",tail)
# 문자열 더하기
print("head + tail = ",head+tail)
# 문자열 곱하기
print("head * 3 = ",head*3)

# 문자열 길이 구하기
a = "Life is too short, You need Python"
print("a : ",a)
print("len(a) = ",len(a))
# 문자열 인덱싱과 슬라이싱
# 인덱싱
print("a[3] = ",a[3])
print("a[-2] = ",a[-2])
# 슬라이싱
print("a[0:4] = ",a[0:4])
# 슬라이싱으로 문자열 나누기
a = "20010331Raniy"
print("a : ",a)
date = a[:8]
print("date = a[:8] : ",date)
weather = a[8:]
print("weather = a[8:] : ",weather)

#문자열 포맷팅
# 바로 대입
print("I eat %d apples."%3)
print("I eat %s apples." %"five")
number = 3
print("I eat %d apples."%number)

# 2개이상의 값 넣기
number = 10
day = "three"

print("I ate %d apples. so I was sick for %s dats." %(number,day))

# 문자열 포맷 코드
# 코드	설명
# %s	문자열(String)
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수
# %%	Literal % (문자 % 자체)

# 포맷코드와 숫자 함께 사용하기
# 정렬과 공백
# %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미이다.
print("%10s"%"hi")
# 왼쪽정렬은 -10
print("%-10sjane"%"hi")
#소수점 표현하기
# %.'의 의미는 소수점 포인트를 말하고 그 뒤의 숫자 4는 소수점 뒤에 나올 숫자의 개수를 말한다.
print("%0.4f"%3.4213234)

# format 함수를 사용한 포맷팅
# 숫자 바로 대입
print("I eat {0} apples".format(3))
# 문자 바로 대입
print("I eat {0} apples".format('five'))
# 숫자 값을 가진 변수로 대입
number = 3
print("I eat {0} apples".format(number))
# 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days".format(number,day))
# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3))
# 왼쪽정렬
print("{0:<10}".format("hi"))
# 오른쪽정렬
print("{0:>10}".format("hi"))
# 가운데정렬
print("{0:^10}".format("hi"))
# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
# {또는}문자 표현하기 - 중괄호 두개 사용
print("{{ and }}".format())

# f 문자열 포맷팅
# 파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용할 수 있다. 파이썬 3.6 미만 버전에서는 사용할 수 없는 기능이므로 주의해야 한다.
name = "홍길동"
age = 30
print(f'나의 이름은 {name} 입니다. 나이는 {age}입니다.')
#  문자열 포매팅은 위와 같이 name, age와 같은 변수 값을 생성한 후에 그 값을 참조할 수 있다. 또한 f 문자열 포매팅은 표현식을 지원하기 때문에 문자열 안에서 변수와 +, -와 같은 수식을 함께 사용할 수 있다.
print(f'나는 내년이면 {age+1}이 된다.')
# 나머지는 위와 동일

# 문자열 관련 함수들
# 문자 개수 세기(count) - 문자열중 해당 문자 개수 확인
a = "hobby"
print(a.count('b'))

# 위치 알려주기1(find) - 문자열 중 해당 문자가 처음 나온 위치를 반환, 찾는문자가 없으면 -1을 반환
a = "Python is the best choice"
print(a.find("b"))
print(a.find('k'))

#위치 알려주기2(index) - 문자열 중 해당 문자가 처음 나온 위치를 반환, 찾는문자가 없으면 오류 발생
a = "Life is too short"
print(a.index("t"))
# print(a.index("k"))

#문자열 삽입(join) - 문자열 사이에 해당 문자를 삽입
print(",".join('abcd'))
# 리스트나 튜플도 사용 가능
print(",".join(['a','b','c','d']))

#소문자를 대문자로 변환(upper)
a = "hi"
print(a.upper())

#대문자를 소문자로 변환(lower)
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기(lstrip)
a = " hi "
print(a.lstrip())

#오른쪽 공백 지우기(rstrip)
print(a.rstrip())

#양쪽 공백 지우기(strip)
print(a.strip())

#문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life","Your leg"))

#문자열 나누기(split) - 괄호안의 값을 넣지않으면 공백(스페이스,탭,엔터 등)을 기준으로 문자열을 나눈다
print(a.split())