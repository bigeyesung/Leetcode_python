def isValidPalindrome(s, k):
    t = s[::-1]
    length = len(s)
    dp = []
    dp = [(length+1)*[0] for j in range(length+1)]

    for i in range(1,length+1):
        for j in range(1,length+1):
            if(s[i-1] == t[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return length - dp[length][length] <= k


ans = isValidPalindrome("adea",1)
print(ans)
    