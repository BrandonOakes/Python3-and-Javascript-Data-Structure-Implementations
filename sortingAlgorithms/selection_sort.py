#Selection Sort Algorithm

#Grab smallest number, put at 0 index, then grab next smallest number
#put at 0+1 index, etc




def selectionSort(array):

    control = True
    original_index = 0

    #iterate current distance of list

    while control:

        #get lowest number

        current_low_value = min(array[original_index:])

        #grab current low value index

        current_low_index = array.index(current_low_value)

        #get first index in current array, this will always be zero because
        #we are shrinking our array distance each iteration

        pointer_index = original_index

        #grab first index  value

        pointer_value = array[pointer_index]

        #swap places of the current low value with the value in the
        #pointer value since the current low value is lower than the
        #poiner value

        array[pointer_index ], array[current_low_index] = current_low_value, pointer_value

        #add 1 to pointer index since we know that location is the lowest

        original_index = ++1

        if pointer_index >= len(array):
            sorted_array = array
            control = False

    return sorted_array

unordered_list = [5,4,3,2,1]

selectionSort(unordered_list)
