# dp[index][diff] equals to the length of arithmetic sequence at index with difference diff.
'''
The main idea is to maintain a map of differences seen at each index.

We iteratively build the map for a new index i, by considering all elements to the left one-by-one.
For each pair of indices (i,j) and difference d = A[i]-A[j] considered, we check if there was an existing chain at the index j with difference d already.

If yes, we can then extend the existing chain length by 1.
Else, if not, then we can start a new chain of length 2 with this new difference d and (A[j], A[i]) as its elements.
At the end, we can then return the maximum chain length that we have seen so far.
'''

def longestArithSeqLength(A):
    #key:index, val: diff
    dp = {}
    for ind1 in range(len(A)):
        for ind2 in range(ind1+1, len(A)):
            pre = (ind1,A[ind2]-A[ind1])
            cur = (ind2,A[ind2]-A[ind1])
            dp[cur] =dp.get(pre,1)+1
    return max(dp.values())

a = [3,6,9,12]
ans = test(a)
print(ans)