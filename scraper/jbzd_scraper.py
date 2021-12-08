import logging

import lxml.html.soupparser as xpath
import requests as requests

from scraper.namer import SimpleNamer
from scraper.scraper import Scraper


class JBZDScraper(Scraper):
    def __init__(self, destination: str):
        self.SOURCE_URL: str = 'https://jbzd.com.pl/'
        self.namer = SimpleNamer(destination)

    def scrap(self, pages_num: int):
        logging.info(f'Scraping from {self.SOURCE_URL} {pages_num} pages into {self.namer.store_location}')
        for page_num in range(1, pages_num):
            page: str = self._fetch_page(page_num)
            urls = self._extract_images_url(page)
            self._download_images(urls)
        # page: str = self._fetch_page(4)
        # self._extract_images_url(page)

    def _fetch_page(self, number: int) -> str:
        url: str = self.SOURCE_URL + 'str/' + str(number)
        logging.debug(f'Fetching page {number}')
        logging.debug(f'Effective url is {url}')
        resp = requests.get(url)
        if resp.ok:
            return resp.text
        else:
            logging.warning(f'Cannot download page {number}')
            raise RuntimeError(f'Cannot download page {number}')

    def _extract_images_url(self, page: str) -> [str]:
        tree = xpath.fromstring(page)
        images = tree.xpath(f"///div[2]/div/a/img")
        logging.info(f'found {len(images)} images')
        urls = []
        for img in images:
            url = img.attrib['src']
            urls.append(url)
        return urls

    def _download_images(self, urls: [str]):
        for url in urls:
            resp = requests.get(url)
            image_name = url.split('/')[-1]
            with open(self.namer.create_name(image_name), 'wb+') as file:
                file.write(resp.content)
