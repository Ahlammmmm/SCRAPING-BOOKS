import re
import logging
from locators.books_locators import BooksLocator


logger = logging.getLogger('scraping.books_parsers')


class BooksParser:
    RATING = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from "{parent}"')
        self.parent = parent

    def __repr__(self):
        return f'<The book {self.title} at {self.link} with the amount {self.price} rated {self.rating}>'

    @property
    def title(self):
        logger.debug('Finding book title...')
        locator = BooksLocator.TITLE
        item_name = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found book title: "{item_name}".')
        return item_name

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BooksLocator.PRICE
        item_price = self.parent.select_one(locator)
        print(item_price)

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f'Found book price: "{float_price}".')
        return float_price

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BooksLocator.LINK
        link_locator = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link: "{link_locator}".')
        return link_locator

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BooksLocator.RATINGS
        item_rating = self.parent.select_one(locator).attrs['class']
        rating_classes = [r for r in item_rating if r != 'star_rating']
        rating_number = BooksParser.RATING.get(rating_classes[0])
        logger.debug(f'Found book rating: "{rating_number}".')
        return rating_number





