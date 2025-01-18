class Solution(object):
    def convert(self, s, numRows):
        if numRows == 0 :
            return ""
        l1 = len(s)
        if l1 <= numRows or numRows == 1:
            return s
        
        result = []
        for iter in range(numRows):
            step = (numRows-1)*2
            for i in range(0, l1, step):
                if i+iter>=l1:
                    continue
                result.append(s[i+iter]) # Collection first value
                if iter == 0 or iter==(numRows-1) or l1<(i+step-iter): # iter: 1, i:4, step: 4 = 4+4-1
                    continue
                result.append(s[i+step-iter])
        return "".join(result)

s1 = Solution()
result = s1.convert("012345678", 10)
print(result)

