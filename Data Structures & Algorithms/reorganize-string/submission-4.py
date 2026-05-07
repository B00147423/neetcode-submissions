class Solution:
    def reorganizeString(self, s: str) -> str:
        
        ##gives uf frequency map of string so we can arrange them
        freq = {}
        result = ""
        for ch in s:
            if ch not in freq:
                freq[ch] = 0
            freq[ch] +=1

        heap = []

        for ch in freq:
            heapq.heappush(heap, (-freq[ch], ch))

        result = []
        prevCount = 0
        prevChar = ""

        while heap:
            count, ch = heapq.heappop(heap)

            result.append(ch)

            if prevCount < 0:
                heapq.heappush(heap, (prevCount, prevChar))

            count += 1

            prevCount = count
            prevChar = ch

        answer = "".join(result)

        if len(answer) != len(s):
            return ""

        return answer