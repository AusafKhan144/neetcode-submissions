class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        matches = {}
        arr = []

        for st in strs:
            sorted_string = ''.join(sorted(st))
            if sorted_string not in matches:
                matches[sorted_string] = [st]
            else:
                matches[sorted_string].append(st)
            
        for values in matches.values():
            arr.append(values)
        
        return arr
