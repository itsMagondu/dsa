def productExceptSelf(nums):
      ans = [1 for _ in nums]
      
      left = 1
      right = 1
      
      for i in range(len(nums)):
          ans[i] *= left
          ans[-1-i] *= right
          left *= nums[i]
          right *= nums[-1-i]
      print (ans)
      return ans

productExceptSelf([1,2,3,4])