import unittest
from selenium_helper import SeleniumHelper

class TestGoogleSearch(unittest.TestCase):

  def test_search_field(self):
   	 SeleniumHelperInstance.initializeWebdriver("Chrome")
   	 SeleniumHelperInstance.navigateToUrl("http://www.google.com")
   	 SeleniumHelperInstance.search("particle detector")
   	 if not SeleniumHelperInstance.waitForPageTitle("particle detector"):
   		 #first close the browser
   		 SeleniumHelperInstance.closeBrowser()
   		 self.fail("Search didn't work.")
   	 SeleniumHelperInstance.closeBrowser()
   		 
if __name__ == '__main__':
    SeleniumHelperInstance = SeleniumHelper()
    unittest.main()