class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for n, f in count.items():
            freq[f].append(n)

        res = []
        for i in reversed(range(len(freq))):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        """

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for n, f in count.items():
            heapq.heappush(heap, (f, n))
            if len(heap) > k:
                heapq.heappop(heap)

        res = [n for (f, n) in heap]
        return res