#
# Create on 5/2/2018
#
# Author: Sylvia
#

"""
452. Minimum Number of Arrows to Burst Balloons
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start
and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the
x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104
balloons.
"""


class Solution:
    @staticmethod
    def find_min_arrow_shots(points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0: return 0
        balloons = sorted(points, key=lambda x: x[1])
        cur_point, shoots = balloons[0][1], 1
        for point in balloons:
            if point[0] > cur_point:
                shoots += 1
                cur_point = point[1]
        return shoots


class Test:
    def test(self):
        assert Solution.find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) is 2
