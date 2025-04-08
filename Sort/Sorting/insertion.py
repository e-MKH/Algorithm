import random
import time

def generate_data(count):
    return [random.gauss(500, 100) for _ in range(count)]

def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def main():
    data_count = int(input("데이터 개수: "))
    trial_count = int(input("시행 횟수: "))

    total_time = 0.0

    for trial in range(trial_count):
        data_set = generate_data(data_count)

        start_time = time.time()
        insertion_sort(data_set)
        end_time = time.time()

        duration = end_time - start_time
        total_time += duration
        print(f"{trial + 1}회차 정렬 시간: {duration:.4f}초")

    average_time = total_time / trial_count
    print(f"\n평균 정렬 시간: {average_time:.4f}초")

if __name__ == "__main__":
    main()
