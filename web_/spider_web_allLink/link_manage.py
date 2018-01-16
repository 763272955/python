# -*- coding:utf-8 -*-
class LinkManager(object):
    def __init__(self):
        self.links_new = set()
        self.links_old = set()

    def link_add_new(self, url):
        if url is None:
            return
        if url not in self.links_new and url not in self.links_old:
            self.links_new.add(url)

    def links_add_new(self, links):
        if links is None or len(links) == 0:
            return
        else:
            for link in links:
                if link not in self.links_new and link not in self.links_old:
                    self.links_new.add(link)

    def link_has_new(self):
        return len(self.links_new) != 0

    def link_get_new(self):
        link_new = self.links_new.pop()
        self.links_old.add(link_new)
        return link_new