
# def palindrome(list1, S, E):
#     list2 = []
#     for i in range(S-1, E, 1):
#         list2.append(list1[i])
    
#     if list2 == list(reversed(list2)):
#         print("S = {}, E = {} 펠리드롬입니다.".format(S, E))
#     else:
#         print("S = {}, E = {} 펠리드롬이 아닙니다.".format(S, E))

# list1 = [1, 2, 1, 3, 1, 2, 1]

# while(True):
#     a, b = map(int, input().split(" "))
#     palindrome(list1, a, b)


def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n-1, 0, -1):
        unsorted[i], unsorted[0] = unsorted[0], unsorted[i]
        heapify(unsorted, 0, i)
    return unsorted[::-1]

unsorted = [12, 30, 6, 7, 4, 13, 8, 11, 50, 24, 2, 5, 10]

print("unsorted = {}".format(unsorted))
print("sorted = {}".format(heap_sort(unsorted)))
