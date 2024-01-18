class FindIndex:
    def Max(self, nums):
        n = len(nums)
        m1 = 0
        m2 = 0

        if n == 0:
            return -1

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                m1 = i
            else:
                m1 = i-1
            if nums[m1] > nums[m2]:
                m2 = m1
            
        return m2

