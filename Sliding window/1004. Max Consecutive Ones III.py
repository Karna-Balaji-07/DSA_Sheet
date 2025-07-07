# 1004. Max Consecutive Ones III


def solutions1(arr,k):
    left = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            k -= 1

        if k < 0:
            if arr[left] == 0:
                k += 1
            left += 1
    return right - left + 1


def findMaxConsecutiveOnes(nums, k):
    left = 0
    zero_count = 0
    max_length = 0

    # Traverse the array using the right pointer
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        # Shrink the window from the left if zero_count exceeds k
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Calculate the maximum length of the valid window
        max_length = max(max_length, right - left + 1)

    return max_length


nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]; k = 3
print(solutions1(nums,k))
