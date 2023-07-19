def canJump( nums):
   """
   :type nums: List[int]
   :rtype: bool
   """
   last_index = len(nums)-1
   reach_dist = 0
   if last_index <= 1:
       return True
   
   for index, jump in enumerate(nums):
       dist = index + jump
       if reach_dist < dist:
           reach_dist = dist
       if reach_dist >= last_index and index != last_index:
           return True
   return False
 
canJump([0,1])