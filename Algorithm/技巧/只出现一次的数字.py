from typing import List
from operator import xor
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)