import random
import time

def generate_data(count):
    return [random.gauss(500, 100) for _ in range(count)]

def heapify(data, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and data[l] > data[largest]:
        largest = l
    if r < n and data[r] > data[largest]:
        largest = r
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heap_sort(data):
    n = len(data)
    for i in range(n//2 - 1, -1, -1):
        heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

def main():
    data_count = int(input("데이터 개수: "))
    trial_count = int(input("시행 횟수: "))
    total_time = 0.0

    for trial in range(trial_count):
        data_set = generate_data(data_count)

        start_time = time.time()
        heap_sort(data_set)
        end_time = time.time()

        duration = end_time - start_time
        total_time += duration
        print(f"{trial+1}회차 정렬 시간: {duration:.4f}초")

    print(f"\n평균 정렬 시간: {total_time / trial_count:.4f}초")

if __name__ == "__main__":
    main()
