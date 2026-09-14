from re import Pattern
from urllib.parse import urljoin

import allure
from playwright.sync_api import Page, expect

from config import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        full_url = urljoin(settings.get_base_url(), url)
        with allure.step(f'Open URL "{full_url}"'):
            self.page.goto(url, wait_until="networkidle")

    def reload(self):
        with allure.step(f'Reload page with URL "{self.page.url}"'):
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(
            f'Check that current URL matches pattern "{expected_url.pattern}"'
        ):
            expect(self.page).to_have_url(expected_url)
