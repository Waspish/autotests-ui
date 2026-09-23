from re import Pattern
from urllib.parse import urljoin

import allure
from playwright.sync_api import Page, expect

from config import settings
from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        full_url = urljoin(settings.get_base_url(), url)
        step = f'Open URL "{full_url}"'

        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until="networkidle")

    def reload(self):
        step = f'Reload page with URL "{self.page.url}"'

        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until="domcontentloaded")

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Check that current URL matches pattern "{expected_url.pattern}"'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
