import logging

from scraper.jbzd_scraper import JBZDScraper


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
    scraper = JBZDScraper('data/jbzd/')
    scraper.scrap(5)


if __name__ == '__main__':
    main()
