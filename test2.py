def find_highest_value(array):
    max_value = array[0]  # Assume the first element is the highest
    max_position = 0  # Position of the current maximum value

    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
            max_position = i

    return max_position