from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class TextArea(BaseElement):
    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator("textarea").first

    def fill(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.fill(text)

    def check_have_value(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(text)
