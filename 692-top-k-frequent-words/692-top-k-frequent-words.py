from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict1=Counter(words)
        sort_dict=dict(sorted(dict1.items()))
        
        res=[]
     
        while k!=0:
            new_value=max(sort_dict,key=sort_dict.get)
            res.append(new_value)
            del sort_dict[new_value]
            k=k-1
            
            
            
        return res