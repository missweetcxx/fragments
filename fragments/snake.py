#
# Create on 2/5/2018
#
# Author: Sylvia
#

"""
Snake
Given a square, walk like a snake as example:
[[0,0], [0,1], [0,2],
 [1,0], [1,1], [1,2],
 [2,0], [2,1], [2,2]]
You should walk as the track: [0,0], [1,0], [2,0], [2,1], [2,2], [1,2], [0,2], [0,1], [1,1]

input: length of side
output: track of moving
"""

import math


class Snake:
    def __init__(self, length):
        self.length = length if length > 0 else 0
        self.square = []
        self.init = [0, 0]

    def generate_square(self):
        square = []
        length = self.length
        if length > 0:
            for i in range(length):
                for j in range(length):
                    square.append([i, j])
            square.remove(self.init)
            self.square = square
        else:
            print ("length of side should greater than 0!")

    def snake_walk(self):
        x, y, pointer, track = 0, 0, 0, [self.init]
        status = range(4)
        count = math.pow(self.length, 2)

        while count > 1:
            tmp_x, tmp_y = x, y
            direction = status[pointer % 4] % 2
            sign = 1 if status[pointer % 4] < 2 else -1
            if direction == 0:
                tmp_x += sign
            else:
                tmp_y += sign

            if [tmp_x, tmp_y] in self.square:
                x, y = tmp_x, tmp_y
                track.append([x, y])
                self.square.remove([x, y])
                count -= 1
            else:
                pointer += 1
        return track


if __name__ == '__main__':
    snake = Snake(3)
    snake.generate_square()
    print (snake.snake_walk())
