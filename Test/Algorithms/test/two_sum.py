class Solution:
    '''
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            x = target - nums[i]
            index = self.find(nums, x)
            if index != -1 and index != i:
                return [i, index]

    def find(self, a, key):
        low = 0
        high = len(a)-1
        while low <= high:
            mid = int(low + (high - low)/2)
            if key < a[mid]: high = mid -1
            elif key > a[mid]: low = mid +1
            else: return mid
        return -1
    '''
 
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums:
                index = nums.index(x)
                if index == i: continue
                else:
                    return [i, index]

if __name__ == "__main__":
    t = Solution()
    r = t.twoSum([3,2,4], 6)
    print(r)