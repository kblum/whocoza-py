import unittest
from whocoza import Scraper


class TestScraperQueryBuilder(unittest.TestCase):
    """
    Test query builder functionality of `Scraper` class.
    """

    def test_class_construction(self):
        expected_domain = 'example.co.za'
        scraper = Scraper(expected_domain)
        self.assertIsNotNone(scraper)
        self.assertEqual(expected_domain, scraper.domain)

    def test_clean_domain(self):
        expected_domain = 'example.co.za'
        scraper = Scraper(expected_domain)
        self.assertEqual(expected_domain, scraper.clean_domain)

    def test_clean_domain_without_co_za(self):
        scraper = Scraper('example')
        self.assertEqual('example.co.za', scraper.clean_domain)

    def test_clean_domain_with_www(self):
        scraper = Scraper('www.example.co.za')
        self.assertEqual('example.co.za', scraper.clean_domain)

    def test_clean_domain_with_http(self):
        scraper = Scraper('http://example.co.za')
        self.assertEqual('example.co.za', scraper.clean_domain)

    def test_clean_domain_with_http_and_www(self):
        scraper = Scraper('http://www.example.co.za')
        self.assertEqual('example.co.za', scraper.clean_domain)

    def test_clean_domain_with_https(self):
        scraper = Scraper('https://example.co.za')
        self.assertEqual('example.co.za', scraper.clean_domain)

    def test_clean_domain_with_https_and_www(self):
        scraper = Scraper('https://www.example.co.za')
        self.assertEqual('example.co.za', scraper.clean_domain)

    def test_clean_domain_with_http_and_trailing_slash(self):
        scraper = Scraper('http://example.co.za/')
        self.assertEqual('example.co.za', scraper.clean_domain)

    def test_query_construction(self):
        scraper = Scraper('example.co.za')
        self.assertEqual('http://co.za/cgi-bin/whois.sh?Domain=example.co.za&Enter=Enter', scraper.query_url)

    def test_none_input(self):
        scraper = Scraper(None)
        self.assertRaises(ValueError, lambda: scraper.clean_domain)
        self.assertRaises(ValueError, lambda: scraper.query_url)

    def test_empty_input(self):
        scraper = Scraper('')
        self.assertRaises(ValueError, lambda: scraper.clean_domain)
        self.assertRaises(ValueError, lambda: scraper.query_url)


if __name__ == '__main__':
    unittest.main()
