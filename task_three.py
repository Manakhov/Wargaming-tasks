def get_minrun(length):
    r = 0
    while length > 63:
        if length & 1:
            r = 1
        length = length >> 1
    return length + r


def sort_run(array, length, minrun):
    for start in range(0, length, minrun):
        end = min(start + minrun - 1, length - 1)
        for i in range(start + 1, end + 1):
            j = i
            while j > start and array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                j = j - 1
    return array


def merge_run(array, length, minrun):
    run = minrun
    while run < length:
        for start in range(0, length, 2*run):
            end = min(start + 2*run - 1, length - 1)
            mid = min(start + run - 1, length - 1)
            left, right = [], []
            for i in range(start, mid + 1):
                left.append(array[i])
            for i in range(mid + 1, end + 1):
                right.append(array[i])
            i_left, i_right = 0, 0
            length_left, length_right = len(left), len(right)
            for i_main in range(start, end + 1):
                try:
                    if left[i_left] < right[i_right]:
                        array[i_main] = left[i_left]
                        i_left = i_left + 1
                    else:
                        array[i_main] = right[i_right]
                        i_right = i_right + 1
                except IndexError:
                    i_break = i_main
                    break
            while i_right < length_right:
                array[i_break] = right[i_right]
                i_right = i_right + 1
                i_break = i_break + 1
            while i_left < length_left:
                array[i_break] = left[i_left]
                i_left = i_left + 1
                i_break = i_break + 1
        run = 2 * run
    return array


def sort(array):
    length = len(array)
    minrun = get_minrun(length)
    array = sort_run(array, length, minrun)
    array = merge_run(array, length, minrun)
    return array
