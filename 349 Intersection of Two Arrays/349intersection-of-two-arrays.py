class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans_set=set()
        for i in nums1:
            for j in nums2:
                if(i==j and i not in ans_set):
                    ans_set.add(i)
        return list(ans_set)
        