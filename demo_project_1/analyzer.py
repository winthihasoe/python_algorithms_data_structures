import time
import random
from demos import quick_sort, mergesort, bubblesort


def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1, max_val))
    return ran_list


size = int(input('What size list do you want to create? '))
max = int(input('What is the max value of the range? '))
run_time = int(input("How many times do you want to run> "))

# def create_random_list(size, max_val):
#     return [random.randint(1,max_val) for num in range(size)]


def analyze_func(func_name, arr):
    tic = time.time()
    func_name(l)
    toc = time.time()
    seconds = toc - tic
    print(f'{func_name.__name__.capitalize()} Elapsed time\t -> {seconds:.5f}')


l = create_random_list(size, max)

for num in range(run_time):
    print("Run", num+1)
    analyze_func(quick_sort, l)
    analyze_func(mergesort, l)
    analyze_func(sorted, l)
    # analyze_func(bubblesort, l.copy)
    print('-' * 40)
