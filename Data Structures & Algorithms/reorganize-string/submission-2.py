class Solution:
    def reorganizeString(self, s: str) -> str:
        
        ##gives uf frequency map of string so we can arrange them
        string_freq = {}
        result = ""
        for ch in s:
            if ch not in string_freq:
                string_freq[ch] = 0
            string_freq[ch] +=1

        while len(result) < len(s):

            bestChar = ""
            bestCount = -1

            for ch in s:
                if string_freq[ch] > 0 and (result == "" or result[-1] != ch):
                    if string_freq[ch] > bestCount:
                        bestChar = ch
                        bestCount = string_freq[ch]

                
            if bestChar == "":
                return ""

            result += bestChar
            string_freq[bestChar] -=1
        return result
        