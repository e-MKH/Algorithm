import random
import time

def generate_data(count):
    return [random.gauss(500, 100) for _ in range(count)]

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

def main():
    data_count = int(input("데이터 개수: "))
    trial_count = int(input("시행 횟수: "))

    total_time = 0.0

    for trial in range(trial_count):
        data_set = generate_data(data_count)

        start_time = time.time()
        selection_sort(data_set)
        end_time = time.time()

        duration = end_time - start_time
        total_time += duration
        print(f"{trial + 1}회차 정렬 시간: {duration:.4f}초")

    average_time = total_time / trial_count
    print(f"\n평균 정렬 시간: {average_time:.4f}초")

if __name__ == "__main__":
    main()
