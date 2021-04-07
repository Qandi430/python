# 집합자료형
# 집합(set)은 파이썬2.3부터 지원하기 시작한 자료형으로, 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
# 집합 자료형은 set키워드를 사용해서 생성 - 리스트를 입력하여 만들거나 문자열을 입력해서 생성 가능
s1 = set([1,2,3])
print(s1)
s2 = set("Hello")
print(s2)

# 집합 자료형의 특징
# 중복을 허용하지 않는다
# 순서가 없다(Unordered)
# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만 
# set은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
# 자료형에서 자정된 값을 인덱싱으로 접근하려면 리스트나 투플로 변환한후 사용
s1 = set([1,2,3])
# print(s1[0])
li = list(s1)
print(li)
print(li[0])
t1 = tuple(s1)
print(t1)
print(t1[0])

# 교집합,합집합,차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
# 교집합 : & or intersection
print(s1 & s2)
print(s1.intersection(s2))
# 합집합 : | or union
print(s1 | s2)
print(s1.union(s2))
# 차집합 : - or difference
print(s1 - s2)
print(s1.difference(s2))

# 집합 자료형 관련 함수들
# 값 1개 추가하기(add)
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가하기(update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
print(s1)