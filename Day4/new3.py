from math import inf
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    n = len(nums)
    nums.sort()
    ans=nums[0]+nums[1]+nums[2]
    mid_diff=inf
    for a in range(n-2):
        if a>0 and nums[a]==nums[a-1]:
            continue
        s=nums[a]+nums[a+1]+nums[a+2]
        if s>target:
            if s - target <mid_diff:
                ans =s
            break
        s = nums[a]+nums[-2]+nums[-1]
        if s<target:
            if target-s<mid_diff:
                mid_diff=target-s
                ans=s
                continue

