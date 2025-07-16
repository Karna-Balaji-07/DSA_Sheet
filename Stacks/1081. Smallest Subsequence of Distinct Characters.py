# 1081. Smallest Subsequence of Distinct Characters
from matplotlib.backends.backend_nbagg import connection_info


def solutions1(s):
    stack = []
    dicts = {character:index for index, character in enumerate(s)}
    visited = set()
    for index, character in enumerate(s):
        if character in visited:
            continue
        while stack and stack[-1] > character and dicts[stack[-1]]> index:
            visited.remove(stack.pop())

        stack.append(character)
        visited.add(character)

    return "".join(stack)

