#
# Create on 6/20/2018
#
#

"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""


class Solution:
    # Manacher algorithm
    # http://en.wikipedia.org/wiki/Longest_palindromic_substring
    @staticmethod
    def longest_palindrome_a(s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        s_j = '#'.join('^{}$'.format(s))
        n = len(s_j)
        P = [0] * n
        id = mx = 0
        for i in range(1, n - 1):
            P[i] = (mx > i) and min(mx - i, P[2 * id - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while s_j[i + 1 + P[i]] == s_j[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > mx:
                id, mx = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]

    @staticmethod
    def longest_palindrome_b(s):
        s_j = '#'.join('^{}$'.format(s))
        if len(s_j) == 3:
            return 0
        max, id = -1, 0
        for i in range(len(s_j)):
            j = 0
            temp = 0
            while j <= i and i + j < len(s_j):
                if s_j[i - j] != s_j[i + j]:
                    break
                temp = j * 2
                j += 1
            if temp > max:
                max = temp
                id = i // 2 - 1
        return s[id - max // 4:id + (max + 1) // 4 + 1] if max % 4 != 0 else s[id - max // 4 + 1:id + max // 4 + 1]

    @staticmethod
    def longest_palindrome_c(s):
        if len(s) == 0:
            return 0
        max, id = -1, 0
        for i in range(len(s)):
            odd_res = Solution._odd(i, max, s, id)
            max, id = odd_res[0], odd_res[1]
            even_res = Solution._even(i, max, s, id)
            max, id = even_res[0], even_res[1]
        return s[id - max // 2:id + (max + 1) // 2] if max % 2 != 0 else s[id - max // 2 + 1:id + max // 2 + 1]

    @staticmethod
    def _odd(i, max, s, id):
        j, temp = 0, 0
        while j <= i and i + j < len(s):
            if s[i - j] != s[i + j]:
                break
            temp = j * 2 + 1
            j += 1
        if temp > max:
            max = temp
            id = i
        return max, id

    @staticmethod
    def _even(i, max, s, id):
        j, temp = 0, 0
        while j <= i and i + j + 1 < len(s):
            if s[i - j] != s[i + j + 1]:
                break
            temp = j * 2 + 2
            j += 1
        if temp > max:
            max = temp
            id = i
        return max, id
