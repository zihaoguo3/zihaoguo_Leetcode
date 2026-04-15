class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        count=0
        new_colors=colors+colors
        for i in range(1,len(colors)+1):
            if new_colors[i]!=new_colors[i-1] and new_colors[i]!=new_colors[i+1]:
                count+=1
        return count


        