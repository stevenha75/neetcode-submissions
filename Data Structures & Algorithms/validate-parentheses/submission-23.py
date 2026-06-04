class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        
        deck = deque()
        for i in range(len(s)):
            if s[i] in closeToOpen:
                if not deck or deck.pop() != closeToOpen[s[i]]:
                    return False
            else:
                deck.append(s[i])

        return not deck