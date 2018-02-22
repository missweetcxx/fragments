#
# Create on 2/22/2018
#
# Author: Sylvia
#

"""
Public Network IP
Find your public network ip (use ip138).
"""

import requests


def get_ip():
    response = requests.get("http://2017.ip138.com/ic.asp").content.decode(errors='ignore')
    ip = str(response.split('[')[1]).split(']')[0]

    return ip


if __name__ == '__main__':
    print('your ip address is : {}'.format(get_ip()))
