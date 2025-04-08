import random
import time

def generate_data(count):
    return [random.gauss(500, 100) for _ in range(count)]

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    data_count = int(input("데이터 개수: "))
    trial_count = int(input("시행 횟수: "))

    total_time = 0.0

    for trial in range(trial_count):
        data_set = generate_data(data_count)

        start_time = time.time()
        data_set = merge_sort(data_set)
        end_time = time.time()

        duration = end_time - start_time
        total_time += duration
        print(f"{trial + 1}회차 정렬 시간: {duration:.4f}초")

    average_time = total_time / trial_count
    print(f"\n평균 정렬 시간: {average_time:.4f}초")

if __name__ == "__main__":
    main()
