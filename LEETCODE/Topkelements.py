class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cuenta = {}
        frec = [[] for n in range(len(nums)+1)]
        for n in nums:
            cuenta[n] = 1 + cuenta.get(n, 0)
        for i, c in cuenta.items():
            frec[c].append(i)
        res = []
        for i in range(len(frec) - 1, 0, -1):
            for n in frec[i]:
                res.append(n)
                if len(res) == k:
                    return res
