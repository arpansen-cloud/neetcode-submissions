class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_ind = {}

        for val in nums:
            if val not in num_ind:
                num_ind[val] = 0

            num_ind[val] += 1

        def get_value(item):

            return item[1]

        ranked = sorted(num_ind.items(), key = get_value, reverse = True )
        
        i = 0
        alist = []
        while i < k:

            alist.append(ranked[i][0])
                    
            i += 1 
        return alist

            





