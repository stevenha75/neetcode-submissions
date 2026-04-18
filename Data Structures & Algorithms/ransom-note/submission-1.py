class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # hashmap
        map = defaultdict(int)

        for c in magazine:
            map[c] += 1
        
        for c in ransomNote:
            map[c] -= 1
            if map[c] < 0:
                return False

        return True