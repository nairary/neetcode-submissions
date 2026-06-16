class Solution:
    def __init__(self):
        self.heap = []
    
    def siftUp(self, stones: List[int], index: int):
        while index > 0:
            parent = (index - 1)//2
            if stones[index] > stones[parent]:
                stones[index], stones[parent] = stones[parent], stones[index]
                index = parent
            else:
                break

    def siftDown(self, stones: List[int], index: int):
        largest = index
        left = index*2+1
        right = index*2+2

        if left < len(stones) and stones[left] > stones[largest]:
            largest = left
        if right < len(stones) and stones[right] > stones[largest]:
            largest = right
        
        if index != largest:
            stones[largest], stones[index] = stones[index], stones[largest]
            self.siftDown(stones, largest)

    def buildHeap(self, stones: List[int]):
        self.heap = stones
        for i in range(len(self.heap)//2-1, -1, -1):
            self.siftDown(self.heap, i)

    def pop(self, heap: List[int]):
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.heap:
            self.siftDown(self.heap, 0)

        return result

    def push(self, heap: List[int], value: int):
        self.heap.append(value)
        self.siftUp(self.heap, len(self.heap)-1)

    def lastStoneWeight(self, stones: List[int]) -> int:
        self.buildHeap(stones)

        while(len(self.heap) > 1):
            first = self.pop(self.heap)
            second = self.pop(self.heap)

            dif = first - second
            if (dif != 0):
                self.push(self.heap, abs(dif))

        if (len(self.heap)):
            return self.heap[0]
        else:
            return 0


