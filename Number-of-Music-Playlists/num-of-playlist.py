def numMusicPlaylists(n, goal, k):
    kMod = 10**9 + 7
    memo = dict()

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0 and j == 0:
            return 1
        if i == 0 or j == 0:
            return 0
        ans = (helper(i - 1, j - 1) * (n - (j - 1)) + helper(i - 1, j) * max(j - k, 0)) % kMod
        memo[(i, j)] = ans
        return ans

    return helper(goal, n)
