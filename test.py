print("Hello to the world")
arr = [8,7,6,3,19,5,3]
for i in range(1,len(arr)):
    if arr[i] >= arr[i-1]:
        print(True)
    else:
        print(False)
