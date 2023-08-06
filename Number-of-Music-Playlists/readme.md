## Number of Music Playlists

In this code, helper(i, j) is a recursive function that calculates the number of playlists of length i using j different songs. If the result is already in the memo dictionary, it returns the cached result. If i or j is 0, it returns 0 or 1 based on whether both are 0. Then it calculates the result based on the two scenarios described in the dynamic programming solution and stores it in the memo dictionary.

The time complexity of this solution is O(n*goal), the same as the dynamic programming solution. Due to the memoization dictionary, the space complexity is also O(n*goal).
