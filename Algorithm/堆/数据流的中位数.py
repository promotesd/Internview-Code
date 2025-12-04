from heapq import heappush, heappushpop

class MedianFinder:

    def __init__(self):
        self.left=[]
        self.right=[]

    def addNum(self, num: int) -> None:
        if len(self.left)==len(self.right):
            heappush(self.left, -heappushpop(self.right, num))
        if len(self.left)>len(self.right):
            heappush(self.right, -heappushpop(self.left, -num))

    def findMedian(self) -> float:

        if self.left>self.right:
            return -self.left[0]
        return (-self.left[0]+self.right[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()