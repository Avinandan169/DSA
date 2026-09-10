class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        #Avinandan169
        arr_set=set(arr)

        current=1

        missing=0

        while True:
            if current not in arr_set:
                missing+=1
                if missing==k:
                    return current
            current+=1
        



        