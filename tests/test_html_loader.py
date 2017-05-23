import unittest
from mock import patch
from bs4 import BeautifulSoup
from jenkins_plugin_change_detector.html_loader import (get_HTML_doc, parse_HTML)


class Test_HTML_Loader(unittest.TestCase):

    def test_get_HTML_doc(self):
        """
        If passed a URL return document data
        """
        url = "https://wiki.jenkins-ci.org/display/JENKINS/Workspace+Cleanup+Plugin"
        self.assertIs(type(get_HTML_doc(url)), unicode)


    def Test_parse_HTML(self):
        """
        Pass html and get html BeautifulSoup class back
        """
        self.assertIs(parse_HTML("<html><body></body></html>"), bs4.BeautifulSoup)
