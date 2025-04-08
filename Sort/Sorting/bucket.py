import random
import time

def generate_data(count):
    return [random.gauss(500, 100) for _ in range(count)]

def bucket_sort(data):
    bucket_count = 10
    max_value = max(data)
    min_value = min(data)
    bucket_range = (max_value - min_value) / bucket_count

    buckets = [[] for _ in range(bucket_count)]

    for num in data:
        index = int((num - min_value) / bucket_range)
        if index == bucket_count:  # max 값이 경계 넘는 경우
            index -= 1
        buckets[index].append(num)

    sorted_data = []
    for bucket in buckets:
        sorted_data.extend(sorted(bucket))  # 각 버킷 정렬

    return sorted_data

def main():
    data_count = int(input("데이터 개수: "))
    trial_count = int(input("시행 횟수: "))
    total_time = 0.0

    for trial in range(trial_count):
        data_set = generate_data(data_count)

        start_time = time.time()
        data_set = bucket_sort(data_set)
        end_time = time.time()

        duration = end_time - start_time
        total_time += duration
        print(f"{trial+1}회차 정렬 시간: {duration:.4f}초")

    print(f"\n평균 정렬 시간: {total_time / trial_count:.4f}초")

if __name__ == "__main__":
    main()
