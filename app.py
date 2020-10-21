import requests
import logging

from pages.books_pages import BooksPage
from parsers.books_parsers import BooksParser

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level=logging.DEBUG,
                    filename='logs.txt',
                    datefmt='%d-%m-%Y %H:%M:%S'
                    )
logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = BooksPage(page_content)

books = page.books

for page_num in range(1, page.pages_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating all BooksPage from page content.')
    page = BooksPage(page_content)
    books.extend(page.books)
