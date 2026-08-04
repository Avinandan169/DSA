class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        answer=[]
        def parting(s,part_list):
            if len(s)==0:
                answer.append(list(part_list))
                return
            for i in range(len(s)):
                part=s[0:i+1]
                if(part[::-1]==part):
                    part_list.append(part)
                    parting(s[i+1:],part_list)
                    part_list.pop()
        parting(s,[])
        return answer

            

            



        
        