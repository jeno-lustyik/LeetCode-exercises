class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()
        rwords = []
        for w in words:
            rwords.append(w[::-1])
        return ' '.join(rwords)

x = Solution()
print(x.reverseWords('Check this backwards'))