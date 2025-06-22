# remove all occurrances of an element in an array

def solution1(arr,element):
    index = 0
    for i in range(len(arr)):
        if arr[i] != element:
            arr[index] = arr[i]
            index += 1

    return index,arr

nums = [0,1,2,2,3,0,4,2];val = 2
print(solution1(nums,val))