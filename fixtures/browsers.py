from typing import Iterator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Iterator[Page]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=f"./tracing/{request.node.name}.zip")
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator(
        "input"
    )
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator(
        "input"
    )
    password_input.fill("password")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    page.wait_for_function("""
            localStorage.getItem('persist:users') &&
            JSON.parse(JSON.parse(localStorage.getItem("persist:users")).user).id != null
        """)

    context.storage_state(path="browser-state.json")

    browser.close()


@pytest.fixture
def chromium_page_with_state(
    initialize_browser_state, request: SubRequest, playwright: Playwright
) -> Iterator[Page]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=f"./tracing/{request.node.name}.zip")
    browser.close()
