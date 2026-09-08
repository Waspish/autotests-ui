from typing import Iterator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Iterator[Page]:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)


@pytest.fixture
def chromium_page_with_state(
    initialize_browser_state, request: SubRequest, playwright: Playwright
) -> Iterator[Page]:
    yield from initialize_playwright_page(
        playwright, storage_state="browser-state.json", test_name=request.node.name
    )


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )
    registration_page.registration_form.fill(
        email="user.name@gmail.com", username="username", password="password"
    )
    registration_page.click_registration_button()

    page.wait_for_function("""
            localStorage.getItem('persist:users') &&
            JSON.parse(JSON.parse(localStorage.getItem("persist:users")).user).id != null
        """)

    context.storage_state(path="browser-state.json")

    browser.close()
