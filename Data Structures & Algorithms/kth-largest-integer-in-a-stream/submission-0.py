class KthLargest:
    def siftDown(self, arr: List[int], index: int) -> List[int]:
        min = index
        left = 2*index+1
        right = 2*index+2
        size = len(arr)

        if left < size and arr[left] < arr[min]:
            min = left
        if right < size and arr[right] < arr[min]:
            min = right

        if min != index:
            arr[min], arr[index] = arr[index], arr[min]
            arr = self.siftDown(arr, min)

        return arr

    def buildHeap(self, arr: List[int]) -> List[int]:
        size = len(arr)
        for i in range(size//2-1, -1, -1):
            arr = self.siftDown(arr, i)
    
        return arr

    def __init__(self, k: int, nums: List[int]):
        size = len(nums)
        self.k = k
        self.heap = []

        for i in range(min(k, size)):
            self.heap.append(nums[i])
        
        self.heap = self.buildHeap(self.heap)

        for i in range(len(self.heap), len(nums)):
            self.add(nums[i])

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self.heap.append(val)
            self.heap = self.buildHeap(self.heap)
        else:
            if self.heap[0] < val:
                self.heap[0] = val
                self.siftDown(self.heap, 0)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)