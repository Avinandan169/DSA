class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_dict={}

        for word in strs:

            sorted_key="".join(sorted(word))
            if(sorted_key not in hash_dict):
                hash_dict[sorted_key]=[]
            
            hash_dict[sorted_key].append(word)
        
        return list(hash_dict.values())
                




            
                        
                    
                    

            

                        




        