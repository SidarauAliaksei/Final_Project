from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url: str) -> None:
        """Base class for the web page
        :param browser: Selenium WebDriver instance
        :param str url: Link to the page
        """
        self.chrome = browser
        self.url = url

    def open(self) -> None:
        """Open the given web page in the browser
        :return: None
        """
        return self.chrome.get(self.url)

    def is_element_present(self, locator) -> bool:
        """Checks if there is an element on the page
        :return: True or False
        """
        try:
            self.chrome.find_element(*locator)
        except NoSuchElementException:
            return False
        return True



