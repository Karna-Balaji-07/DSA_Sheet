# Make String a Subsequence Using Cyclic Increments

def solution(s1,s2):
    index = 0
    for i in s1:
        next_char = 'a' if i == 'z' else chr(ord(i)+1)
        if index < len(s2):
            if s2[index] in (i, next_char):
                index += 1

    return index == len(s2)

