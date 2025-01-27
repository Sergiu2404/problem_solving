def brute_force(interval_size, array):
    i = 0
    curr_max = float('-inf')

    if len(array) <= interval_size:
        return sum(array)

    while i + interval_size < len(array):
        sum_interval = 0
        for j in range(interval_size):
            sum_interval += array[i + j]

        curr_max = curr_max if curr_max > sum_interval else sum_interval
        i += 1

    return curr_max


# print(brute_force(4, [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 10]))


def sliding_window(window_size, array):
    curr_sum = 0
    curr_max = 0

    for j in range(window_size):
        curr_sum += array[j]

    start = 0
    end = window_size
    while end < len(array):
        curr_sum = curr_sum - array[start] + array[end]
        curr_max = max(curr_sum, curr_max)
        start += 1
        end += 1

    return curr_max

print(sliding_window(4, [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 10]))