#
# Create on 1/30/2018
#
# Author: Sylvia
#

"""
Counter
Count number of time for each word occurs in a file, and list most common words with corresponding occurrence times.
"""

import io
import re
from os import path

from config import ROOT_PATH


class Counter:
    def __init__(self, path):
        self.mapping = dict()
        with io.open(path, encoding='utf-8') as f:
            data = f.read()
            words = [s.lower() for s in re.findall("\w+", data)]
            for word in words:
                self.mapping[word] = self.mapping.get(word, 0) + 1

    def most_common(self, n):
        assert n > 0
        return sorted(self.mapping.items(), key=lambda item: item[1], reverse=True)[:n]


if __name__ == '__main__':
    poem_path = path.join(ROOT_PATH, 'resources/poem.txt')
    most_common_5 = Counter(poem_path).most_common(5)

    for item in most_common_5:
        print(item)
