class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)

        for each in strs:
            key="".join(sorted(each))
            ans[key].append(each)
        return list(ans.values())
                

        