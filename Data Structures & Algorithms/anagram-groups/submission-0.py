class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #given a list which contains multiple strs , maybe we sort it based on the lenght of he str, then we spearate the str based on the lenghts the we use the sorted function to check if they are anagrams
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)
        return list(groups.values())
        