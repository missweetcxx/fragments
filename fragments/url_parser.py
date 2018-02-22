#
# Create on 2/22/2018
#
# Author: Sylvia
#

"""
URL Parser
Given a URL, parse it into schema, netloc, path, params and fragments.

"""

from collections import namedtuple

URL = namedtuple("URL", ["schema", "netloc", "path", "params", "fragments"])


def url_parser(url):
    schema = path = params = fragments = None
    path_flag, param_dict = True, {}

    schema_len = url.find('://')
    # get schema
    if schema_len > 0 and url.startswith('http'):
        schema, url = url[:schema_len], url[schema_len + 3:]

    # get netloc
    for item in '/?#':
        netloc_len = url.find(item)
        if netloc_len > 0:
            netloc, url = url[:netloc_len], url[netloc_len:]
            break
    else:
        netloc, path_flag = url, False

    # get path
    if path_flag:
        for item in '?#':
            path_len = url.find(item)
            if path_len > 0:
                path, url = url[:path_len], url[path_len:]
                break
        else:
            path = url

    # get params and fragments
    if '#' in url:
        url, fragments = url.split('#', 1)
    if '?' in url:
        try:
            url, param = url.split('?', 1)
            param_items = param.split('&')
            for item in param_items:
                param_dict[item.split('=')[0]] = item.split('=')[1]
            params = param_dict
        except Exception:
            raise TypeError

    return URL._make([schema, netloc, path, params, fragments])


if __name__ == '__main__':
    url_tuple = url_parser('https://www.test.com/to/my/path?user=1&name=a#something')
    print('schema : {}'.format(url_tuple[0]))
    print('netloc: {}'.format(url_tuple[1]))
    print('path : {}'.format(url_tuple[2]))
    print('params : {}'.format(url_tuple[3]))
    print('fragments: {}'.format(url_tuple[4]))
