def counting_sort(array):
    max_val = max(array)
    min_val = min(array)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    for i in range(len(array)):
        count[array[i] - min_val] += 1
    j = 0
    for i in range(range_of_elements):
        while count[i] > 0:
            array[j] = i + min_val
            count[i] -= 1
            j += 1
    return array

a = [5,5,1,0,0,2,3,3,2,4]
print("array before sorting: ", a)
b = counting_sort(a)
print("array after sorting: ", b)