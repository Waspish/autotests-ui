from playwright.sync_api import Page

from components.courses.course_list_toolbar_view_component import (
    CourseListToolbarViewComponent,
)
from components.courses.course_view_component import CourseViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page=page, identifier="courses-list")
        self.course_view = CourseViewComponent(page)
        self.toolbar_view = CourseListToolbarViewComponent(page)

        # Заголовок и кнопка создания курса
        self.courses_title = self.page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_button = self.page.get_by_test_id(
            "courses-list-toolbar-create-course-button"
        )

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here",
        )
