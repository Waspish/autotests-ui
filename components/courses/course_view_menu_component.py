import allure

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.menu_button = Button(
            page=page, locator="course-view-menu-button", name="Menu"
        )
        self.edit_menu_item = Button(
            page=page, locator="course-view-edit-menu-item", name="Edit"
        )
        self.delete_menu_item = Button(
            page=page, locator="course-view-delete-menu-item", name="Delete"
        )

    @allure.step('Open course menu at index "{index}" and click edit')
    def click_edit_course(self, index: int):
        self.menu_button.check_visible(nth=index)
        self.menu_button.click(nth=index)

        self.edit_menu_item.check_visible(nth=index)
        self.edit_menu_item.click(nth=index)

    @allure.step('Open course menu at index "{index}" and click delete')
    def click_delete_course(self, index: int):
        self.menu_button.check_visible(nth=index)
        self.menu_button.click(nth=index)

        self.delete_menu_item.check_visible(nth=index)
        self.delete_menu_item.click(nth=index)
