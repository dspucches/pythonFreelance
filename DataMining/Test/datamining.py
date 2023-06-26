# Name: Dominic Spucches
# Date: 5/9/2023
# Project: Url Scraping - Total Malware Data by location
# Description: The purpose of this project is to conduct data mining tool that scrapes websites for
# data that pertain to the total websites that talk about malware by geolocation.
# Notes: insure to use a proxy, import urls to scan as a list

import zenrows      # evades CAPTCHAs and antibots
import scrapy       # open-source tool, extract data from websites, fast high-level web crawling
import requests     # Requests allow the user to sent requests to the HTTP server and GET response back in the form of HTML or JSON response. It also allows the user to send POST requests to the server to modify or add some content.
import io           #  automatically check scraped data and perform QA audits at regular intervals
import selenium     #   automatically check scraped data and perform QA audits at regular intervals
import unittest


from selenium import webdriver

browser = webdriver.Edge()           # chooses browser and places inside variable
browser.get('http://selenium.dev/')     # opens url 'http://selenium.dev/' using the browser stored in variable 'browser'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()

browser.get('http://www.google.com')
assert "Yahoo" in browser.title

elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()

from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)