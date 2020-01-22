import multiprocessing
import time

start = time.perf_counter()

def FunctionOne():
    print("Function one is sleeping for 1 second.")
    time.sleep(1)

def FunctionTwo():
    print("Function two is sleeping for 1 second.")
    time.sleep(1)

def FunctionThree():
    i = a = 0
    b = 1
    while i < 10:
        print(a)
        i = i + 1
        c = a + b
        a = b
        b = c

process_1 = multiprocessing.Process(target=FunctionOne)
process_2 = multiprocessing.Process(target=FunctionTwo)
process_3 = multiprocessing.Process(target=FunctionThree)

process_1.start()
process_2.start()
process_3.start()

process_1.join()
process_2.join()
process_3.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')

processing = []

for _ in range(10):
    process_1 = multiprocessing.Process(target=FunctionOne)
    process_2 = multiprocessing.Process(target=FunctionTwo)
    process_3 = multiprocessing.Process(target=FunctionThree)
    process_1.start()
    process_2.start()
    process_3.start()
    processing.append(process_1)
    processing.append(process_2)
    processing.append(process_3)

for process in processing:
    process.join()

