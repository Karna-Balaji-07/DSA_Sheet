def solution(arr, query):
    arr.sort(key=lambda x: x[0])
    result = []

    for i in query:
        low = 0
        high = len(arr) - 1
        maximum = float('-inf')

        while low <= high:
            mid = (low + high) // 2
            if arr[mid][0] <= i:
                # Move right, but also scan backwards from mid to find max beauty ≤ i
                temp = mid
                # Go left to include all values ≤ i (as duplicates exist)
                while temp >= 0 and arr[temp][0] <= i:
                    maximum = max(maximum, arr[temp][1])
                    temp -= 1
                low = mid + 1
            else:
                high = mid - 1

        result.append(maximum if maximum != float('-inf') else 0)

    return result

def solution2(arr,query):
    arr.sort()
    prices = []
    prefix = []
    beauty = float('-inf')
    for price,beauties in arr:
        beauty = max(beauty,beauties)
        prices.append(price)
        prefix.append(beauty)
    
    result = []
    for i in query:
        low = 0
        high = len(arr)-1
        index = -1
        while low <= high:
            mid = (low+high)//2
            if prices[mid] <= i:
                index  = mid
                low = mid+1
            else:
                high = mid-1
            
        if index != -1:
            result.append(prefix[index])
        else:
            result.append(0)
        return result
    
                
