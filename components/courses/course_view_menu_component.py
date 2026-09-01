from playwright.sync_api import expect

from components.base_component import BaseComponent


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.menu_button = self.page.get_by_test_id("course-view-menu-button")
        self.edit_menu_item = self.page.get_by_test_id("course-view-edit-menu-item")
        self.delete_menu_item = self.page.get_by_test_id("course-view-delete-menu-item")

    def click_edit_course(self, index: int):
        expect(self.menu_button.nth(index)).to_be_visible()

        expect(self.edit_menu_item.nth(index)).to_be_visible()
        self.edit_menu_item.nth(index).click()

    def click_delete_course(self, index: int):
        expect(self.menu_button.nth(index)).to_be_visible()

        expect(self.delete_menu_item.nth(index)).to_be_visible()
        self.delete_menu_item.nth(index).click()
