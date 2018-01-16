# -*- coding:utf-8 -*-

import requests

class HtmlDownloader(object):
    def downloader(self, link):
        if link is None:
            return
        else:
            response = requests.get(link)
            response.encoding = requests.utils.get_encodings_from_content(response.content)[0]
            if response.status_code != 200:
                return
            else:
                return response.text