class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            visited[key].append(s)

        return list(visited.values())
