# 고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다. 공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.
# round() 함수를 사용해서, 다음과 같이 소수점 아래 네 자리까지 출력해 보세요.
count = 1
height = 100
while count <= 10:
    height = height/(5/3)
    print(count, round(height,4))
    count += 1
