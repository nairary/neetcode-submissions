class Point:
    def __init__(self, coords: List[int]):
        self.x = coords[0]
        self.y = coords[1]
        self.distance = self.x**2 + self.y**2

class Solution:
    def __init__(self):
        self.heap = []
        self.points = []

    def pop(self) -> Point:
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.heap:
            self.siftDown(0)
        
        return result

    def push(self, value: Point) -> None:
        self.heap.append(value)
        size = len(self.heap)
        if size > 1:
            self.siftUp(size-1)

    def siftDown(self, index: int) -> None:
        left = 2*index+1
        right = 2*index+2
        min_index = index
        size = len(self.heap)

        if (left < size and self.heap[left].distance < self.heap[min_index].distance):
            min_index = left
        if (right < size and self.heap[right].distance < self.heap[min_index].distance):
            min_index = right
        
        if min_index != index:
            self.heap[min_index], self.heap[index] = self.heap[index], self.heap[min_index]
            self.siftDown(min_index)

    def siftUp(self, index: int) -> None:
        parent = (index-1)//2
        if index == 0:
            return

        if self.heap[index].distance < self.heap[parent].distance:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.siftUp(parent)

    def buildHeap(self) -> None:
        for i in range(len(self.heap)//2-1, -1, -1):
            self.siftDown(i)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            self.heap.append(Point(point))

        self.buildHeap()
        result = []
        for i in range(k):
            p = (self.pop())
            result.append([p.x, p.y])

        return result        