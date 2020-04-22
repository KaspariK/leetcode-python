from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valid_sums = []

        # Sort the list because we are going to iterate through and for each
        # number will use a 2 pointer sliding window on the remaining numbers
        nums.sort()

        for i, num in enumerate(nums):
            # Check for duplicates as we shouldn't be including these in our response
            if i > 0 and num == nums[i - 1]:
                continue

            left_ptr = i + 1
            right_ptr = len(nums) - 1

            # Our target number is the additive inverse of the current num
            target = 0 - num

            while left_ptr < right_ptr:
                # If the number is too high or too low, we need to move a pointer
                if nums[left_ptr] + nums[right_ptr] > target:
                    right_ptr -= 1
                elif nums[left_ptr] + nums[right_ptr] < target:
                    left_ptr += 1
                else:
                    valid_sums.append([num, nums[left_ptr], nums[right_ptr]])

                    # We now need to check if the next value for our pointer is going to be the same,
                    # if it is, it will result in a duplicate so we need to move our pointer further
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr + 1]:
                        left_ptr += 1
                    while left_ptr < right_ptr and nums[right_ptr] == nums[right_ptr - 1]:
                        right_ptr -= 1

                    # Now that we know the next pointer value isn't a duplicate we can move them as normal
                    left_ptr += 1
                    right_ptr -= 1

        return valid_sums


s = Solution()
print(s.threeSum(
    [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
