import random

# 반복 횟수
iterations = 10000
total_count = 0  # 누적 개수

for i in range(1, iterations + 1):
    # 평균=500, 표준편차=100인 정규분포 데이터 100개 생성
    data = [random.gauss(500, 100) for _ in range(100)]

    # 400 이상 600 이하인 값의 개수 세기
    count = 0
    for value in data:
        if 400 <= value <= 600:
            count += 1

    # 각 시행 결과 출력
    print(f"{i:3}번째 시행: 400~600 사이 데이터 개수 = {count}")

    total_count += count

# 평균 계산
average_count = total_count / iterations
print(f"\n10000번 시행의 평균 개수: {average_count:.3f}개")
