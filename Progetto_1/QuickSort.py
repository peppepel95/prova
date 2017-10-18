def partition(myList, start, end, key, reverse):
    pivot = myList[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and _lessEqualNode(myList[left], pivot, key, reverse):
            left = left + 1
        while _greaterEqualNode(myList[right], pivot, key, reverse) and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            # swap places
            temp = myList[left]
            myList[left] = myList[right]
            myList[right] = temp
    # swap start with myList[right]
    temp = myList[start]
    myList[start] = myList[right]
    myList[right] = temp
    return right


def quicksort(myList, start, end, key=None, reverse=False):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end, key, reverse)
        # sort both halves
        quicksort(myList, start, pivot - 1, key, reverse)
        quicksort(myList, pivot + 1, end, key, reverse)
    return myList


def _lessEqualNode(val1, val2, key, reverse):
    if reverse:
        return _greaterEqualNode(val1, val2, key, False)
    if key == None:
        return val1 <= val2
    else:
        return key(val1) <= key(val2)


def _greaterEqualNode(val1, val2, key, reverse):
    if reverse:
        return _lessEqualNode(val1, val2, key, False)
    if key == None:
        return val1 >= val2
    else:
        return key(val1) >= key(val2)
