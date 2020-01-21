    def longestPalindrome(self, s: str) -> str:
        # repeat question, input, output
        # cornor case empty string
        # test case
        # sudo code
        # len1, len2, len>=3......
        size = len(s)
        if size ==0:
            return ""
        
        p = [[False]*size for i in range(size)]
        start = 0
        
        #length = 1
        length = 1
        for ind in range(size):
            p[ind][ind]=True
            start = ind
            
        #length = 2
        length = 2
        for ind in range(size-1):
            if s[ind] == s[ind+1]:
                p[ind][ind+1] = True
                start = ind
        #length >= 3
        for l in range(3,size+1):
            for i in range(size-l+1):
                j = i+l-1
                if p[i+1][j-1] and s[i]==s[j]:
                    p[i][j] = True
                    start = i
                    length = l
                    
        return s[start:start+length]