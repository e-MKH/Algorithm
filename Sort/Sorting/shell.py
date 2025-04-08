import random
import time

def generate_data(count):
    return [random.gauss(500, 100) for _ in range(count)]

def shell_sort(data):
    n = len(data)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 2

def main():
    data_count = int(input("데이터 개수: "))
    trial_count = int(input("시행 횟수: "))
    total_time = 0.0

    for trial in range(trial_count):
        data_set = generate_data(data_count)

        start_time = time.time()
        shell_sort(data_set)
        end_time = time.time()

        duration = end_time - start_time
        total_time += duration
        print(f"{trial+1}회차 정렬 시간: {duration:.4f}초")

    print(f"\n평균 정렬 시간: {total_time / trial_count:.4f}초")

if __name__ == "__main__":
    main()
