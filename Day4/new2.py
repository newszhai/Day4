from typing import List


def twoSum(number: List[int], targe: int) -> List[int]:
    left = 0
    right = len(number) - 1
    while True:
        s = number[left] + number[right]
        if s == targe:
            return [left + 1, right + 1]
        if s < targe:
            left += 1
        else:
            right -= 1


number=[2,7,11,13]
targe = 9
print(twoSum(number, targe))