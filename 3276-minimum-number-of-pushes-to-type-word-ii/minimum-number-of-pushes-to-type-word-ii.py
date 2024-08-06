class Solution:
    def minimumPushes(self, word: str) -> int:
        l=[0]*(32)
        for i in range(26):
            l[i]=word.count(chr(97+i))
        l.sort(reverse=True)
        res=0
        for i in range(4):
            for j in range(8):
                res+=(i+1)*l[8*i+j]
        return res
"""
        # Count letter occurrences
        letter_counts = [0] * 26
        for char in input_text:
            letter_counts[ord(char) - ord('a')] += 1
        
        # Sort counts in descending order
        sorted_counts = sorted(letter_counts, reverse=True)
        
        total_key_presses = 0
        for index, count in enumerate(sorted_counts):
            if count == 0:
                break
            total_key_presses += (index // 8 + 1) * count
        
        return total_key_presses
"""