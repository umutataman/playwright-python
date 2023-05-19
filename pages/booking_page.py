from datetime import datetime

import phonenumbers
from playwright.sync_api import Page


class BookingPage:
    def __init__(self, page: Page) -> None:
        self.page = page.context.pages[-1] if len(page.context.pages) > 1 else page

    def fill_primary_passenger_details(self, email, phone_number, firstname, lastname, nationality, gender, dob,
                                       passport_number, passport_expiry_date):
        self.page.fill("//input[@name='email']", email)
        # Filling phone number
        parsed_number = phonenumbers.parse(phone_number)
        country_code = phonenumbers.region_code_for_country_code(parsed_number.country_code).lower()
        national_number = str(parsed_number.national_number)
        self.page.select_option("//select[@name='phoneCountry']", value=country_code)
        self.page.fill("//input[@name='phone']", national_number)
        # Filling passenger details
        self.page.fill("//input[@name='firstname']", firstname)
        self.page.fill("//input[@name='lastname']", lastname)
        self.page.select_option("//select[@name='nationality']", nationality)
        self.page.select_option("//select[@name='title']", gender)
        # Filling date of birth
        parsed_date = datetime.strptime(dob, "%d-%m-%Y")
        day = parsed_date.strftime("%d")
        month = parsed_date.strftime("%B")
        year = parsed_date.strftime("%Y")
        self.page.fill("//input[@name='birthDay']", day)
        self.page.select_option("//select[@name='birthMonth']", month)
        self.page.fill("//input[@name='birthYear']", year)
        # Filling passport details
        self.page.fill("//input[@name='idNumber']", passport_number)
        parsed_date = datetime.strptime(passport_expiry_date, "%d-%m-%Y")
        day = parsed_date.strftime("%d")
        month = parsed_date.strftime("%B")
        year = parsed_date.strftime("%Y")
        self.page.fill("//input[@name='idExpirationDay']", day)
        self.page.select_option("//select[@name='idExpirationMonth']", month)
        self.page.fill("//input[@name='idExpirationYear']", year)

    def remove_second_traveler(self):
        self.page.click("(//button[@data-test='removePassengerButton'])[2]")

    def click_continue(self):
        self.page.click("//button[@data-test='StepControls-passengers-next']")
