import logging
import random

import pytest
from playwright.sync_api import Page


class SearchResultsPage:
    def __init__(self, page: Page) -> None:
        self.page = page.context.pages[-1] if len(page.context.pages) > 1 else page

    def wait_for_search_results(self):
        # TODO: add a few more loading indicators
        self.page.wait_for_selector("//div[@data-test='BookingButton']", state="visible")

    def apply_filters_stop(self, stop):
        self.page.click(f"//span[normalize-space()='{stop}']")

    def apply_filters_exclude_country(self, country):
        self.page.click("//div[contains(text(),'Exclude countries')]")
        self.page.click("//div[contains(text(),'Search countries')]")
        self.page.fill("//input[@placeholder='Search countries']", country)
        if self.page.is_visible(f"//span[contains(text(),'{country}')]"):
            self.page.click(f"//span[contains(text(),'{country}')]")
        else:
            logging.info(f"The country is not available for exclude: {country}")

    def select_any_flight(self):
        flights = self.page.query_selector_all("//div[@data-test='ResultCardWrapper']")
        return random.randint(1, len(flights))

    def verify_flight_stops(self, selected_flight):
        stops = self.page.inner_text(
            f"//div[@data-test='ResultCardWrapper'][{selected_flight}]//div[@data-test='StopCountBadge-1']")
        stops = stops.replace(" • Change airport", "").replace(" • Change airports", "")
        return stops

    def click_select_for_booking(self, selected_flight):
        self.page.click(f"//div[@data-test='ResultCardWrapper'][{selected_flight}]//div[@data-test='BookingButton']")

    def click_continue_as_guest(self):
        self.page.click("//a[@data-test='MagicLogin-GuestTextLink']")
