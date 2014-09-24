class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s=s.split()
        s=s[::-1]
        return " ".join(s)