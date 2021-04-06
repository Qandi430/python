# 원금(Principal), 이율(rate), 기간(time)이 주어졌을 때, 이자(Interest)를 구하는 공식은 다음과 같습니다.

# I=Prt
# 그리고 원리금(Amount)을 구하는 공식은 다음과 같습니다.

# A=P(1+rt)
def simple_interest(p,r,t):
    return p*r*t

def simple_interest_amount(p,r,t):
    return p * (1+r*t)

print(simple_interest(10000000, 0.03875, 5))
print(simple_interest(1100000, 0.05, 5/12))

print(simple_interest_amount(10000000, 0.03875, 5))
print(simple_interest_amount(1100000, 0.05, 5/12))