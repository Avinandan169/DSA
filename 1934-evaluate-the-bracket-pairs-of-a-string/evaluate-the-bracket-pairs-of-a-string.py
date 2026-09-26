class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        #Avinandan169
        know_map=dict(knowledge)
        
        res=[]
        curr_key=[]
        in_bracket=False
        
        for ch in s:
            if ch=='(':
                in_bracket=True
            elif ch==')':
                key_str = "".join(curr_key)
                res.append(know_map.get(key_str, "?"))
                curr_key=[]
                in_bracket=False
            elif in_bracket:
                curr_key.append(ch)
            else:
                res.append(ch)
                
        return "".join(res)