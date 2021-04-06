# P′=P(1+rn)nt
# P′ : 원리금
# P : 원금
# r : 연이율
# t : 기간
# n : 복리 횟수


def compound_interest_amount(p,r,t,n) :
    return p * (1 + r / n) ** (n * t)

print(compound_interest_amount(1500000, 0.043, 6, 4))
print(compound_interest_amount(1500000, 0.043, 6, 1/2))
print(compound_interest_amount(3600000, 0.058, 2, 1))