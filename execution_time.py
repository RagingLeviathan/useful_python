import timeit
import time

start_time = timeit.timeit()
# Code to check follows
a, b = 1, 2
c = a + b
# Code to check ends
end_time = timeit.timeit()
time_taken_in_micro = (end_time - start_time)*(10**6)

print(" Time taken in micro_seconds: {0} ms".format(time_taken_in_micro))

print(time.time(), time.process_time(), time.perf_counter())
time.sleep(1)
print(time.time(), time.process_time(), time.perf_counter())
