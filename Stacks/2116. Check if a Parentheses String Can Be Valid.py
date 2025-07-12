class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stringlength = len(s)
        if stringlength % 2 == 1:
            return False

        opens = []
        unlock = []
        for i in range(stringlength):
            if locked[i] == '0':
                unlock.append(i)
            elif s[i] == '(':
                opens.append(i)
            elif s[i] == ')':
                if opens:
                    opens.pop()
                elif unlock:
                    unlock.pop()
                else:
                    return False

        while opens and unlock and opens[-1] < unlock[-1]:
            opens.pop()
            unlock.pop()

        if not opens and unlock:
            return len(unlock) % 2 == 0

        return not opens