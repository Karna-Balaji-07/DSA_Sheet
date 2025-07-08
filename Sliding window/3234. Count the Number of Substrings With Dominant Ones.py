# 3234. Count the Number of Substrings With Dominant Ones

def solutions(s):
    left = 0
    right = 0
    arr = ""
    count =0
    while right < len(s):
        arr += s[right]
        zeros = arr.count('0')
        ones = arr.count('1')
        if ones == 0:
            right += 1
            continue

        if ones <= zeros**2:
            arr = arr[1:]
            left += 1
            if left == right:
                right += 1
            continue

        if ones >= zeros**2:
            count += 1
            right += 1

    return count


def solutions1(s):
    count = 0
    n = len(s)
    for i in range(n):
        ones = 0
        zeros = 0
        for j in range(i, n):
            if s[j] == '1':
                ones += 1
            else:
                zeros += 1
            if ones >= zeros ** 2:
                count += 1
    return count


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        vals = [-1]
        for key, value in enumerate(s):
            one = zeros = 0
            if value == '1':
                one += 1
            else:
                zeros += 1
            p = key
            for k in reversed(vals):
                one += p - k - 1
                result += max(0, min(p - k, one - zeros ** 2 + 1))
                p = k
                zeros += 1
                if zeros ** 2 > key:
                    break
            if value == '0':
                vals.append(key)

        return result


s = "00011"
print(solutions(s))  # Output: 2


s = "101101"
print(solutions1(s))
s = "00011"
print(solutions(s))