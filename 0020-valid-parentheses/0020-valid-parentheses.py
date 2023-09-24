class Solution:
    def isValid(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '"':
                continue
            if c in "([{":
                stack.append(c)
            if c in ")]}":
                if len(stack) > 0:
                    p = stack.pop()
                    if p == "(" and c != ")":
                        return False
                    if p == "[" and c != "]":
                        return False
                    if p == "{" and c != "}":
                        return False
                else:
                    return False
        return True if len(stack) == 0 else False


'''
parsez stringul
pun in queue paranteza daca este de tip deschidere
cand intalnesc tip inchidere, pop, verific daca e la fel
daca nu e return fals
daca reusesc sa parsez tot si stack empty true
'''
