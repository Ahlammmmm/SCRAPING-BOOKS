import re
import logging

from bs4 import BeautifulSoup

from locators.pages_locators import PagesLocator
from parsers.books_parsers import BooksParser


logger = logging.getLogger('scraping.books_pages')


class BooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML Parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using "{PagesLocator.BOOKLOCATOR}".')
        locator = PagesLocator.BOOKLOCATOR
        books_locator = self.soup.select(locator)
        return [BooksParser(e) for e in books_locator]

    @property
    def pages_count(self):
        logger.debug('Finding the number of available pages...')
        locator = PagesLocator.PAGER
        page_locator = self.soup.select_one(locator).string
        logger.info(f'Found number of catalogue pages available: "{page_locator}".')

        pattern = 'Page [0-9]+ of ([0-9]+)'          #() for entities that don't change
        matcher = re.search(pattern, page_locator)
        pages = int(matcher.group(1))                #group(0) : is all the expression and group(1) : is the entity with ()
        logger.debug(f'Extracted number of pages as integer: "{pages}".')
        return pages
