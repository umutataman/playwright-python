import os
import shutil

import allure
import pytest
from allure_commons.types import AttachmentType
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.booking_page import BookingPage


# TODO: Remove this fixture when combined all allure results into one
@pytest.fixture(autouse=True)
def clear_allure_results(request):
    allure_results_dir = './reports/allure-results'
    shutil.rmtree(allure_results_dir, ignore_errors=True)
    os.makedirs(allure_results_dir, exist_ok=True)
    yield


@pytest.fixture
def result_page(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def result_page(page: Page) -> SearchResultsPage:
    return SearchResultsPage(page)


@pytest.fixture
def result_page(page: Page) -> BookingPage:
    return BookingPage(page)


@pytest.hookimpl(tryfirst=True)
def pytest_bdd_step_error(request, step, step_func_args):
    # Get the page object from step function arguments
    # page = step_func_args["page"]
    page = request.getfixturevalue('page')
    screenshot = page.screenshot()
    allure.attach(screenshot, name='Screenshot', attachment_type=AttachmentType.PNG)
