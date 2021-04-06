# 다음 triple() 함수를 완성하세요.
# >>> def triple(x):
# ...     ██████ █ █ █
# ... 
# >>> triple(2)
# 6
# >>> triple('x')
# 'xxx'

def triple(x):
    return x * 3

print(triple(2))
print(triple('x'))

# 문제 2
# 오늘의 날짜 객체를 구하는 코드는 다음과 같습니다. (코드를 이해하지 못해도 이 문제를 풀 수 있습니다.)

# >>> from datetime import datetime
# >>> today = datetime.today()
# >>> today
# datetime.datetime(2021, 3, 21, 15, 46, 1, 94942)
# 위 코드의 today에서 연도를 구하는 방법은 다음과 같습니다.

# >>> today.year
# 2021
# 태어난 해를 네 자리 숫자로 입력하면 한국 나이를 반환하는 함수 korean_age()를 작성하세요.

from datetime import datetime


def korean_age(year) :
    return datetime.today().year - year +1

print(korean_age(1990))
    
