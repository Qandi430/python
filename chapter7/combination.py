from itertools import permutations
from itertools import combinations
items = ['A','B','C','D','E','F']
raffle5 = []
raffle4 = []
raffle3 = []
raffle2 = []

for i in list(combinations(items,5)):
    raffle5.append(i)

for i in list(combinations(items,4)):
    raffle4.append(i)

for i in list(combinations(items,3)):
    raffle3.append(i)

for i in list(combinations(items,2)):
    raffle2.append(i)

for i in raffle5:
    print(i)

print("\n")

for i in raffle4:
    print(i)

print("\n")

for i in raffle3:
    print(i)

print("\n")

for i in raffle2:
    print(i)


