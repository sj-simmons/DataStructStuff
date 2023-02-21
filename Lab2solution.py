
def FindMax(lst):
    """return the maximum element"""

    current_max = lst[0]

    for i in range(len(lst)):
        element = lst[i]
        if element > current_max:
            current_max = element

    return current_max

test_list = [17*i % 2023 for i in range(10000)]

print(FindMax(test_list))
