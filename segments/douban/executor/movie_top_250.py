#!/usr/bin/env python
# -*- coding: utf-8 -*-

from segments.douban.common.constants import FilePath
from segments.douban.config import CONFIG
from segments.douban.utils.clear_file_util import ClearFile
from segments.douban.utils.movie_datum_util import MovieDatum
from segments.douban.utils.output_util import OutputUtils


def get_movies_datum(id):
    movie_items = MovieDatum.get_movie_etree(id)
    for item in movie_items:
        print(CONFIG['FORMAT']['TOP_OUTPUT'].format(item['id'], item['title'], item['score'], item['desc']))

        with open(FilePath.RECORDS_PATH, 'ab+') as f:
            tmp_data = CONFIG['FORMAT']['TOP_OUTPUT'].format(item['id'], item['title'], item['score'],
                                                             item['desc']) + "\n"
            f.write(tmp_data.encode("utf-8"))
        img_addr = str(item['img_addr'][0].replace("\'", ""))
        OutputUtils.download_img(item['id'], item['title'], img_addr)


def main():
    # clear files
    ClearFile.clear_all()

    # get top250 movie info
    ids = [i * 25 for i in range(10)]
    for id in ids:
        get_movies_datum(id)


if __name__ == '__main__':
    main()
