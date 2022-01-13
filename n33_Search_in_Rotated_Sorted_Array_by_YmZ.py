class Solution:
    def find_index(self,nums):
        start = 0
        end = len(nums)-1
            
        while(start < end):
            mid = math.floor((start + end)/2)
            if(nums[mid] < nums[0]):
                end = mid
            else:
                start = mid + 1
        return start  
    
    def binary_search(self, nums, start, end, target):
        while(start <= end):
            mid = math.floor((start + end)/2)
            if(nums[mid] < target):
                start = mid + 1
            elif(nums[mid] > target):
                end = mid - 1
            elif(nums[mid] == target):
                return mid
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        index = self.find_index(nums)
        
        if(nums[index] <= target and nums[len(nums)-1] >= target):
            return self.binary_search(nums,index,len(nums)-1,target)
        
        else:
            return self.binary_search(nums,0,index-1,target)