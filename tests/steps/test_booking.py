from pytest_bdd import given, when, then, parsers, scenarios
from sttable import parse_str_table

from pages.home_page import HomePage as HP
from pages.search_results_page import SearchResultsPage as SRP
from pages.booking_page import BookingPage as BP

# Scenarios

scenarios('booking.feature')


@given('I am on the Kiwi.com website')
def open_kiwi_website(page):
    HP(page).open()


@given('I am on the Kiwi.com website and accept cookies')
def open_kiwi_website(page):
    HP(page).open()
    HP(page).accept_cookies()


@when(parsers.parse('I select a flight from "{departure}" to "{destination}"'))
def search_flight(page, departure, destination):
    HP(page).flights_from_to(departure, destination)


@when(parsers.parse('I set the departure date as "{departure_date}"'))
def set_departure_date(page, departure_date):
    HP(page).set_departure_date(departure_date)


@when(parsers.parse('I set the return date as "{return_date}"'))
def set_return_date(page, return_date):
    HP(page).set_return_date(return_date)


@when(parsers.parse('I set the number of passengers as "{num_passengers}"'))
def set_num_passengers(page, num_passengers):
    HP(page).set_num_passengers(num_passengers)


@when('I click on the search button')
def click_search_button(page):
    HP(page).click_search_button()


@when('I wait for the search results to load')
def wait_for_search_results(page):
    SRP(page).wait_for_search_results()


@when(parsers.parse('I select the filter option for "{stop}" and excluding "{country}"'))
def apply_filters_one_stop_ex_uk(page, stop, country):
    SRP(page).apply_filters_stop(stop)
    SRP(page).apply_filters_exclude_country(country)


@when('I select any flight from the search results')
def select_any_flight(page, context):
    context.random_flight = SRP(page).select_any_flight()


@then(parsers.parse('I verify that the selected flight has {stop} stop'))
def verify_flight_stops(page, stop, context):
    stops = SRP(page).verify_flight_stops(context.random_flight)
    expected_stops = f"{stop} stop" if stop == "1" else f"{stop} stops"
    assert stops == expected_stops, f"Expected {expected_stops} stops, but found {stops} stops."


@when('I click on the "Select" button for booking')
def click_select_for_booking(page, context):
    page = page.context.pages[-1] if len(page.context.pages) > 1 else page
    SRP(page).click_select_for_booking(context.random_flight)


@when('I click "Continue as a guest" button')
def click_continue_as_guest(page):
    SRP(page).click_continue_as_guest()


@when(parsers.parse('I complete the required fields on the checkout form page\n{data_table}'))
def fill_checkout_form(page, data_table):
    data = parse_str_table(data_table).rows[0]
    BP(page).fill_primary_passenger_details(
        data["Email"],
        data["Phone Number"],
        data["Firstname"],
        data["Lastname"],
        data["Nationality"],
        data["Gender"],
        data["Date of Birth"],
        data["Passport Number"],
        data["Passport Expire Date"]
    )


@when('I remove second traveler button')
def remove_traveler(page):
    BP(page).remove_second_traveler()


@when('I click on the "Continue" button')
def click_continue_button(page):
    BP(page).click_continue()
