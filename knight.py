	
def knightDialer(N):    
    mv = { 0: [4, 6], 1 : [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]  }
    rs = [1]*10
    for i in range(N-1):
        tmp = [0]*10
        for j in range(10):
            for k in mv[j]:
                tmp[j] += rs[k]
        
        rs = tmp

    return sum(rs) % ((10**9) + 7)

ans = knightDialer(3)
print(ans)