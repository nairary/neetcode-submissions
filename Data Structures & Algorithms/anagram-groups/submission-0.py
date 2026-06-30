class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for line in strs:
            embeding = [0]*26
            for ch in line:
                embeding[ord(ch)-ord('a')]+=1
                
            key = tuple(embeding)

            if key not in hash_map:
                hash_map[key] = []
            
            hash_map[key].append(line)

        result = []
        for key, value in hash_map.items():
            result.append(value)
        
        return result