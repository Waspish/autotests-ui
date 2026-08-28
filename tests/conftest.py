from typing import Iterator

import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Iterator[Page]:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
