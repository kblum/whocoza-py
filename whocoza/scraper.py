import re


class Scraper(object):

    query_url_format_string = 'http://co.za/cgi-bin/whois.sh?Domain={0}&Enter=Enter'

    def __init__(self, domain):
        """
        Construct new instance of .co.za scraper for a given domain.
        :param domain: Name of domain to run query on.
        :return:
        """
        self.domain = domain
        self.__clean_domain = None  # underlying value for lazy property

    @staticmethod
    def _clean_domain(domain):
        if not domain:
            # no input provided, therefore invalid domain
            raise ValueError("No domain provided.")
        try:
            r = re.compile("(?:https|http)?(?:://)?(?:www\.)?([^/\r\n]+)(/[^\r\n]*)?")
            clean_domain = r.findall(domain)[0][0]
        except IndexError:
            return ValueError("Invalid domain.")
        if not clean_domain.endswith('.co.za'):
            clean_domain += '.co.za'
        return clean_domain

    @property
    def clean_domain(self):
        """
        Get the clean representation of the given domain.
        Returns `None` if the given domain is not valid.
        :return: string
        """
        if self.__clean_domain is None:
            self.__clean_domain = self._clean_domain(self.domain)
        return self.__clean_domain

    @property
    def query_url(self):
        """
        Get URL to perform whois query for domain.
        :return: string
        """
        if not self.clean_domain:
            # domain is invalid, therefore a query URL cannot be constructed
            raise ValueError("Invalid domain.")
        return self.query_url_format_string.format(self.clean_domain)
