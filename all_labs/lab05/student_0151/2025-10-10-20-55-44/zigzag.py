# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(nums):
  if len(nums) < 3:
    return True

  for i in range(1, len(nums) - 1):
    # Current element
    mid = nums[i]
    left = nums[i - 1]
    right = nums[i + 1]

    if not ((mid > left and mid > right) or (mid < left and mid < right)):
      return False

  return True