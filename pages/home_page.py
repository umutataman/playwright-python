from datetime import datetime

from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self):
        self.page.goto("https://www.kiwi.com/en/")

    def accept_cookies(self):
        if self.page.is_visible("//*[@data-test='CookiesPopup-Accept']"):
            self.page.click("//*[@data-test='CookiesPopup-Accept']")
        self.page.wait_for_selector("//div[@data-test='CookiesPopup-Accept']", state="hidden")

    def open_passenger_field(self):
        self.page.click("//div[@data-test='PassengersField']")

    def wait_city_picker(self, destinations):
        self.page.wait_for_selector(f"//div[@data-test='PlacePickerRow-city']//div[contains(text(),'{destinations}')]",
                                    state="visible")

    def passenger_field_done(self):
        self.page.click("//button[@data-test='PassengersFieldFooter-done']")

    def flights_from_to(self, departure, destinations):
        import shutil
        shutil.rmtree("screenshots", ignore_errors=True)
        self.page.click("//div[@data-test='SearchPlaceField-origin']")
        self.page.click("//div[@data-test='PlacePickerInputPlace-close']")
        self.page.fill("//div[@data-test='PlacePickerInput-origin']/input", departure)
        self.wait_city_picker(departure)
        self.page.click(f"//div[@data-test='PlacePickerRow-city']")
        self.page.fill("//div[@data-test='PlacePickerInput-destination']/input", destinations)
        self.wait_city_picker(destinations)
        self.page.click(f"//div[@data-test='PlacePickerRow-city']")

    def click_date(self, date):
        parsed_date = datetime.strptime(date, "%d-%m-%Y")
        month_year = parsed_date.strftime("%B %Y")
        date = parsed_date.strftime("%Y-%m-%d")
        while not self.page.is_visible(f"//div[contains(text(),'{month_year}')]"):
            self.page.click("//button[@aria-label='Next month']")

        # If the date on right, there are being 2 elements with the same data-value if the day is
        date_elements = self.page.query_selector_all(f"//div[@data-value='{date}']")
        if len(date_elements) > 1:
            date_elements[1].click()
        else:
            date_elements[0].click()

    def close_date_picker(self):
        self.page.click("//button[@data-test='SearchFormDoneButton']")

    def set_departure_date(self, departure_date):
        self.page.click("//input[@name='search-outboundDate']")
        self.click_date(departure_date)
        self.close_date_picker()

    def set_return_date(self, return_date):
        self.page.click("//input[@name='search-inboundDate']")
        self.click_date(return_date)
        self.close_date_picker()

    def set_num_passengers(self, num_passengers):
        self.open_passenger_field()
        # get value of current passengers byt input value
        current_passenger = self.page.query_selector("//div[@data-test='PassengersRow-adults']//input").input_value()
        if int(num_passengers) != int(current_passenger):
            for i in range(1, int(num_passengers)):
                self.page.click("//div[@data-test='PassengersRow-adults']//button[@aria-label='increment']")
        self.passenger_field_done()

    def click_search_button(self):
        self.page.click("//div[contains(text(),'Search')]")
