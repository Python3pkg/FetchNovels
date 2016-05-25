#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from novel import single, utils, const

BASE_URL = 'http://www.cool18.com/bbs4/index.php?app=forum&act=threadview&tid={}'


class Cool18Tool(utils.Tool):

    def __init__(self):
        super().__init__()
        self.remove_extras.extend((
            re.compile(r'www\.6park\.com'),
            re.compile(r'<.*?bodyend.*?>.*')
        ))


class Cool18(single.Novel):

    def __init__(self, tid, proxies=None):
        super().__init__(utils.base_to_url(BASE_URL, tid),
                         'pre',
                         title_sel=('name', 'Description'),
                         title_type=single.TitleType.meta,
                         headers=const.HEADERS, proxies=proxies,
                         tool=Cool18Tool)


def main():
    utils.in_main(Cool18, const.GOAGENT, overwrite=False)


if __name__ == '__main__':
    main()