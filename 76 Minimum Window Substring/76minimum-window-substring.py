class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m=len(s)
        n=len(t)
        if(m<n):
            return ""
        left,right=0,0
        start_idx=-1
        cut=0
        hash={}
        min_len=10**5
        for i in t:
            hash[i]=hash.get(i,0)+1
        
        while(right<m):
            right_char=s[right]

            if right_char in hash:
                if hash[right_char]>0:
                    cut+=1
                hash[right_char]-=1


            while(cut==n):
                if(right-left+1<min_len):
                    min_len=right-left+1
                    start_idx=left
                left_char=s[left]
                if left_char in hash:
                    hash[left_char]+=1
                    if hash[left_char]>0:
                        cut-=1
                left+=1  
            right+=1
        return "" if start_idx==-1 else s[start_idx:start_idx+min_len]






        