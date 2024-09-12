public class Solution {
    public int CountConsistentStrings(string allowed, string[] words) {
        // Step 1: Generate bitmask for allowed characters
        int allowedMask = 0;
        foreach (char c in allowed) {
            allowedMask |= (1 << (c - 'a'));  // Set the bit for the character
        }

        int consistentCount = 0;

        // Step 2: Iterate through each word
        foreach (string word in words) {
            int wordMask = 0;

            // Step 3: Generate bitmask for the current word
            foreach (char c in word) {
                wordMask |= (1 << (c - 'a'));  // Set the bit for the character
            }

            // Step 4: Check if the word is consistent
            if ((wordMask & allowedMask) == wordMask) {
                consistentCount++;  // The word is consistent
            }
        }

        return consistentCount;
    }
}