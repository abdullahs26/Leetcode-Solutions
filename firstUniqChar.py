class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)

        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
            
        return -1
