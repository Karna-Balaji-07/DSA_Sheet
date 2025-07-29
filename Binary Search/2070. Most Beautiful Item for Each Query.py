# 2070. Most Beautiful Item for Each Query

def solution(arr,query):
    arr.sort(key=lambda  x:x[0])
    result = []
    for i in query:
        low = 0
        high = len(arr)-1
        maximum = 0
        while high >= low:
            mid = (low+high)//2
            if arr[mid][0] > i:
                high = mid-1
            elif arr[mid][0] <= i:
                temp = mid
                while temp >= 0 and arr[temp][0] <= i:
                    maximum = max(maximum, arr[temp][1])
                    temp -= 1
                    
                low = mid+1
        result.append(maximum)
    
    return result

items = [[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]
queries = [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]
print(solution(items,queries))