class BasePage:
    def __init__(self, page):
        self.page = page

    def create_new_page(self):
        # Get the browser instance from the current page
        browser = self.page.context.browser

        # Create a new page instance
        new_page = browser.new_page()

        # Return the new page instance
        return new_page

    def switch_to_page(self, page):
        # Switch to the specified page
        self.page = page

    def get_page_title(self):
        title = self.page.title()
        return title