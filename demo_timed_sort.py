import time
from random import randint, sample

def selection_sort(lst):
    """Use selection sort to return lst sorted in increasing order."""
    for i in range(len(lst)):
        indexOfMin = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[indexOfMin]:
                lst[j], lst[indexOfMin] = lst[indexOfMin], lst[j]
    return lst

assert selection_sort(sample(range(100), 100)) == list(range(100))

def insertion_sort(lst):
    """Use selection sort to return lst sorted in increasing order."""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

assert insertion_sort(sample(range(100), 100)) == list(range(100))

import bisect

def binary_insertion_sort(lst):
    """Use binary insertion sort to return lst sorted in increasing order."""
    for i in range(1, len(lst)):
        key = lst[i]
        insert_at = bisect.bisect(lst[:i], key)
        lst = lst[:insert_at] + [key] + lst[insert_at:i] + lst[i+1:]
    return lst

assert binary_insertion_sort(sample(range(100), 100)) == list(range(100))

# helper for merge sort
def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    """Use merge sort to return lst sorted in increasing order."""
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

assert merge_sort(sample(range(100), 100)) == list(range(100))

def gen_list(n):
    """Generate a random list of length n of integers in {1,...,1000000}."""
    rlist = []
    for i in range(n):
        rlist.append(randint(1,10000000))
    return rlist

def time_sort(lst, sorting_algo):
    """Return how many seconds it takes for sort_algo to sort lst."""
    start=time.time()
    sorting_algo(lst)
    finish=time.time()
    print(finish-start)

def time_built_in_sort(lst):
    start=time.time()
    lst.sort()
    finish=time.time()
    print(finish-start)

def main():

    sort = selection_sort; print("selection sort:")
    print("sorting 1000 numbers: ", end=' ')
    time_sort(gen_list(1000), sort)
    print("sorting 10000 numbers:", end=' ')
    time_sort(gen_list(10000), sort)

    sort = insertion_sort; print("\ninsertion sort:")
    print("sorting 1000 numbers: ", end=' ')
    time_sort(gen_list(1000), sort)
    print("sorting 10000 numbers:", end=' ')
    time_sort(gen_list(10000), sort)

    #sort = binary_insertion_sort; print("\nbinary insertion sort")
    #print("sorting 1000 numbers: ", end=' ')
    #time_sort(gen_list(1000), sort)
    #print("sorting 10000 numbers:", end=' ')
    #time_sort(gen_list(10000), sort)

    sort = merge_sort; print("\nmerge sort:")
    print("sorting 1000 numbers: ", end=' ')
    time_sort(gen_list(1000), sort)
    print("sorting 10000 numbers:", end=' ')
    time_sort(gen_list(10000), sort)

    #time_sort(gen_list(100000), sort)
    #time_built_in_sort(gen_list(100000))
    #time_built_in_sort(gen_list(1000000))

main()


