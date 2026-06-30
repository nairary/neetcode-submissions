class Solution:
    def pop(self, hash_map: Dict(), heap: List[int]) -> int:    
        result = heap[0]
        if len(heap) == 1:
            heap.pop()
            return result

        heap[0] = heap.pop(-1)
        self.siftDown(hash_map, heap, 0)
        return result

    def siftDown(self, hash_map: Dict(), heap: List[int], k: int):
        index = k
        
        if 2*k+1 < len(heap) and hash_map[heap[index]] < hash_map[heap[2*k+1]]:
            index = 2*k+1
        if 2*k+2 < len(heap) and hash_map[heap[index]] < hash_map[heap[2*k+2]]:
            index = 2*k+2
        
        if index != k:
            heap[k], heap[index] = heap[index], heap[k]
            self.siftDown(hash_map, heap, index)

    def siftUp(self, hash_map: Dict(), heap: List[int], k: int):
        parent = (k-1)//2
        if (k != 0 and hash_map[heap[k]] >= hash_map[heap[parent]]):
            heap[k], heap[parent] = heap[parent], heap[k]
            self.siftUp(hash_map, heap, parent)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num]=1
            else:
                hash_map[num]+=1
            
            heap.append(num)
            self.siftUp(hash_map, heap, len(heap)-1)
        
        result = set()
        counter = 0
        for i in range(0, len(heap)):
            if counter == k:
                break

            curr = self.pop(hash_map, heap)
            if curr not in result:
                counter+=1
                result.add(curr)
        
        return list(result)