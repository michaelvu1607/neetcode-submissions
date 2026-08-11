class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}

        for str in strs:
            if "".join(sorted(str)) in strs_dict:
                strs_dict["".join(sorted(str))].append(str)

            else:
                strs_dict["".join(sorted(str))] = [str]
        
        return list(strs_dict.values())