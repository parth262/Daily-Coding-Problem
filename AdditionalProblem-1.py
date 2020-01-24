'''
Return a new sorted merged list from K sorted lists, each with size N
'''

from collections import _heapq

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]

    # basically sorting the array of tuple
    _heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = _heapq.heappop(heap)
        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1], list_ind, element_ind+1)
            _heapq.heappush(heap, next_tuple)
    return merged_list


result = merge([[13, 15, 40], [12, 15, 20], [17, 20, 32]])

print(result)