from random import randrange
import timeit


def BubbleSort(unsorted_list):
    start = timeit.default_timer()

    for unsorted_index in range(0, len(unsorted_list)):
        for current_index in range(0, (len(unsorted_list) - unsorted_index - 1)):
            if unsorted_list[current_index] > unsorted_list[current_index+1]:
                unsorted_list[current_index], unsorted_list[current_index+1] = \
                    unsorted_list[current_index+1], unsorted_list[current_index]

    end = timeit.default_timer()

    time_taken = end - start

    print(f"Bubble Sort Algorithm list: {unsorted_list}\n"
          f"Bubble Sort Time Taken: {round(time_taken, 10)} seconds")


def SelectionSort(unsorted_list):
    start = timeit.default_timer()

    for index in range(0, len(unsorted_list)):
        current_min_value = unsorted_list[index]
        current_index_min = index
        for compare_index in range(index, len(unsorted_list)):
            if unsorted_list[compare_index] < current_index_min:
                current_min_value = unsorted_list[compare_index]
                current_index_min = compare_index
            unsorted_list[index], unsorted_list[current_index_min] = \
                unsorted_list[current_index_min], unsorted_list[index]

    end = timeit.default_timer()

    time_taken = end - start

    print(f"Selection Sort Algorithm list: {unsorted_list}\n"
          f"Selection Sort Time Taken: {round(time_taken, 10)} seconds")


def InsertionSort(unsorted_list):

    start = timeit.default_timer()

    for index in range(1, len(unsorted_list)):
        set_value = unsorted_list[index]
        j = index

        while j > 0 and unsorted_list[j - 1] > set_value:
            unsorted_list[j] = unsorted_list[j - 1]
            j = j - 1
        unsorted_list[j] = set_value

    end = timeit.default_timer()
    time_taken = end - start

    print(f"Insertion Sort Algorithm list: {unsorted_list}\n"
          f"Insertion Sort Time Taken: {round(time_taken, 10)} seconds")


random_list = [randrange(1, 500000) for _ in range(0, 10000)]
print(random_list)

BubbleSort(random_list)

SelectionSort(random_list)

InsertionSort(random_list)
