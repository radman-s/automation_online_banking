from lxml import etree

class Root:

    def __init__(self, page_source, locator):
        self.tree = etree.HTML(page_source)
        self.locator = locator

    def get_listings(self, listing):
        divs = self.tree.findall(self.locator)
        return [listing(div) for div in divs]


