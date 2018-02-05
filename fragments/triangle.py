#
# Create on 2/5/2018
#
# Author: Sylvia
#

"""
Triangle
Given a triangle, find the minimun path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.
For Example, given the following triangle:

[
       [2],
     [3],[4],
   [6],[5],[7],
 [4],[1],[8],[3]
 ]
"""


class Triangle:
    def minimumTotal(self, triangle):
        for r in range(len(triangle) - 1)[::-1]:
            for l in range(len(triangle[r])):
                left = triangle[r][l] + triangle[r + 1][l]
                right = triangle[r][l] + triangle[r + 1][l + 1]
                triangle[r][l] = min(left, right)
        return triangle[0][0]


def main():
    result = Triangle().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print("Minimun sum is {}".format(result))


if __name__ == '__main__':
    main()
