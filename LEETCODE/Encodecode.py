class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            k = str(len(i))
            res += k + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != "#"):
                j += 1
            lon = int(s[i:j])
            res.append(s[j+1: j+1+lon])
            i = j+1+lon
        return res
