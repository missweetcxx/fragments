#
# Create on 5/2/2018
#
# Author: Sylvia
#

"""
406. Queue Reconstruction by Height
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater than
or equal to h. Write an algorithm to reconstruct the queue.
"""


class Solution(object):
    @staticmethod
    def reconstruct_queue(people):
        if not people: return []
        peopledct, height, res = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()

        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res


class Test:
    def test(self):
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        assert Solution.reconstruct_queue(people) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
