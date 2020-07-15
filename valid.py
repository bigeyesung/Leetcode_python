    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        left = []
        right = []
        product = 1
        
        for ind in range(0,len(nums)):
            left.append(product)
            product = nums[ind]*product
            
        product = 1
        for ind in range(len(nums)-1,-1,-1):
            right.append(product)
            product = nums[ind]*product
        
        for ind in range(0, len(nums)):
            tmp = left[ind]*right[len(nums)-1-ind ]
            ans.append(tmp)
        return ans       