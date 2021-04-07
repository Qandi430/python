# 자료형의 값을 저장하는 공간,변수
# 변수 생성 - 변수명 = 저장할 값
a = 1
b = "python"
c = [1,2,3]

# 변수란 객체를 가리키는 것
a = [1,2,3]
# 위 코드 처럼 a = [1,2,3] 이라고 하면 [1,2,3] 값을 가지는 리스트 자료형(객체)이 자동으로 메모리에 생서되고 변수 a는 [1,2,3] 리스트가 저장된 메모리의 주소를 가르키게 된다.
# id 는 객체의 주소값을 돌려주는 파이썬 내장함수이다.
print(id(a))


# 리스트를 복사하고자 할 때 
a = [1,2,3]
b = a
print(a)
print(b)
a[2] = 4
print(a)
print(b) 
# b변수에 a변수를 대입하면 같은 주소값을 공유하기에 a의 요소를 바꾸면 b의 요소도 바뀐다

# a의 값을 가져오면서 다른 주소를 가리키도록 만드는 방법
# [:]이용
a = [1,2,3]
b = a[:]
print(a)
print(b)
a[2] = 4
print(a)
print(b)

# copy 모듈 이용
a = [1,2,3]
from copy import copy
b = copy(a)
print(a)
print(b)
a[2] = 4
print(a)
print(b)


# 변수를 만드는 여러가지 방법
# 튜플로 a,b에 값 대입
a,b = ('python','life')
print(a,b)
# 튜플은 괄호를 생략가능
(a,b) = 'python','life'
print(a,b)
# 리스트로 변수 생성
[a,b] = ['python','life']
# 여러개의 변수에 같은 값을 대입
a = b = 'python'
print(id(a),id(b))
