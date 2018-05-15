#
# Create on 5/8/2018
#
# Author: Sylvia
#

"""
93. Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
"""


class Solution(object):
    def __init__(self, s):
        """
        :type s: str
        """
        self.s = s
        self.results = []

    def restore_ip_addresses(self):
        """
        :rtype: List[str]
        """
        self._helper(0, 0, [])

    def _helper(self, start, k, result):
        if k == 4:
            if start == len(self.s):
                self.results.append('.'.join(result))
            else:
                return
        if k < 4:
            for i in range(1, 4):
                if i != 3 or 0 < int(self.s[start: start + i]) < 256:
                    self._helper(start + i, k + 1, result + [str(int(self.s[start:start + i]))])
        return


class Test:
    def test(self):
        res = Solution('25505511135')
        res.restore_ip_addresses()
        assert len(res.results) == 2
        for ip in ['255.55.11.135', '255.55.111.35']:
            assert ip in res.results
