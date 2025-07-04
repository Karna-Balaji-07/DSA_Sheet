# 567. Permutation in String

from itertools import permutations

def solutions1(string, test):
    perms = permutations(string)
    arr = [''.join(p) for p in perms]
    k = len(string)
    for i in range(len(test)-k+1):
        sub = test[i:i+k]
        if sub in arr:
            return True
    return False

def checkInclusion(self, s1: str, s2: str) -> bool:
	cntr, w, match = Counter(s1), len(s1), 0

	for i in range(len(s2)):
		if s2[i] in cntr:
			if not cntr[s2[i]]: match -= 1
			cntr[s2[i]] -= 1
			if not cntr[s2[i]]: match += 1

		if i >= w and s2[i-w] in cntr:
			if not cntr[s2[i-w]]: match -= 1
			cntr[s2[i-w]] += 1
			if not cntr[s2[i-w]]: match += 1

		if match == len(cntr):
			return True

	return False

s1 = "a"; s2 = "ab"
print(solutions1(s1,s2))