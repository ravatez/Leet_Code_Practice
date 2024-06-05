class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Step 1: Convert each word into a character frequency map
        word_freq = [Counter(word) for word in words]
        
        # Step 2: Find the intersection of all the character frequency maps
        common_freq = word_freq[0]
        for freq in word_freq[1:]:
            common_freq = common_freq & freq
        
        # Step 3: Create a result list by iterating over the common characters
        result = []
        for char, count in common_freq.items():
            result.extend([char] * count)
        
        return result    