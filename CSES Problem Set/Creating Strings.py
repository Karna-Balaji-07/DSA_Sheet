def Permutations(arr, ans, index):
    if index == len(arr):
        ans.append(arr[:])
        return
    for i in range(index, len(arr)):
        arr[i], arr[index] = arr[index], arr[i]
        Permutations(arr, ans, index + 1)
        arr[i], arr[index] = arr[index], arr[i]  # backtrack

s = input().strip()
arr = list(s)
ans = []
Permutations(arr, ans, 0)

# Convert to string permutations
result = ["".join(i) for i in ans]

# Remove duplicates (if characters are repeated), then sort
unique_result = sorted(set(result))

# Output
print(len(unique_result))
for item in unique_result:
    print(item)
