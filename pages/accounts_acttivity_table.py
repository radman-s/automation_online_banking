class Listings:

    def __init__(self, listing_div):
        self.id = int(listing_div.find('./td[1]').text)
        self.date = listing_div.find('./td[2]').text
        self.name = listing_div.find('./td[3]').text
        self.amount = listing_div.find('./td[4]').text
        self.balance = listing_div.find('./td[5]').text


