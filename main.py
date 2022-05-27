from Tasks import Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8

import time

# test_Task1

assert Task1.binary_to_decimal([0, 1, 1, 0]) == 6

print(Task2.wave("hello world"))

# test_Task4

assert Task4.get_strong_string(
    "будем искать самое сильное слово в произвольной строке") == "Слово произвольной победило, набрав 13015 баллов"

# test_Task5

assert Task5.the_inside_out_string("synchronization") == "orhcnysnnoitazi"

# test_Task6

assert Task6.roman_to_arabic("DCCCLXXXVIII") == 888

print(Task8.time_from_pattern(time.time(), "%Y-%m-%d"))

wave_ = Task3.wave_eternal("hello world")
for _ in range(20):
    print(next(wave_))
