from typing import Pattern

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.button = Button(
            page=page, locator=f"{identifier}-drawer-list-item-button", name="Sidebar"
        )
        self.icon = Icon(
            page=page, locator=f"{identifier}-drawer-list-item-icon", name="Sidebar"
        )
        self.title = Text(
            page=page,
            locator=f"{identifier}-drawer-list-item-title-text",
            name="Title",
        )

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        self.button.check_visible()
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(
            title,
        )

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)
