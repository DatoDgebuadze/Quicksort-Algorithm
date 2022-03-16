# Ascending order
# In this algotithm we will take one number as a base and compare it with the rest of the numbers
# for example let's take 5 as a base in Ascending order.......

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

## input any data you want down in this format, this is just an example.
print(quick_sort([5,3,2,1,4]))