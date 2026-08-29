from dataclasses import dataclass

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


@dataclass
class CourseCardData:
    index: int
    title: str
    max_score: str
    min_score: str
    estimated_time: str


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.title = self.page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_button = self.page.get_by_test_id(
            "courses-list-toolbar-create-course-button"
        )

        # Карточка курса
        self.course_title = self.page.get_by_test_id("course-widget-title-text")
        self.course_image = self.page.get_by_test_id("course-preview-image")
        self.course_max_score_text = self.page.get_by_test_id(
            "course-max-score-info-row-view-text"
        )
        self.course_min_score_text = self.page.get_by_test_id(
            "course-min-score-info-row-view-text"
        )
        self.course_estimated_time_text = self.page.get_by_test_id(
            "course-estimated-time-info-row-view-text"
        )

        # Меню курса
        self.course_menu_button = self.page.get_by_test_id("course-view-menu-button")
        self.course_menu_edit_option = self.page.get_by_test_id(
            "course-view-edit-menu-item"
        )

        self.course_menu_delete_option = self.page.get_by_test_id(
            "course-view-delete-menu-item-text"
        )

        # Пустой блок при отсутсвии курсов
        self.empty_view_icon = self.page.get_by_test_id("courses-list-empty-view-icon")
        self.empty_view_title = self.page.get_by_test_id(
            "courses-list-empty-view-title-text"
        )
        self.empty_view_description = self.page.get_by_test_id(
            "courses-list-empty-view-description-text"
        )

    def click_create_course_button(self):
        self.create_course_button.click()

    def verify_title_displayed_correctly(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("Courses")

    def verify_empty_view_visible(self):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text("There is no results")

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text(
            "Results from the load test pipeline will be displayed here"
        )

    def verify_course_card_visible(self, params: CourseCardData):
        expect(self.course_title.nth(params.index)).to_be_visible()
        expect(self.course_title.nth(params.index)).to_have_text(params.title)

        expect(self.course_image.nth(params.index)).to_be_visible()

        expect(self.course_max_score_text.nth(params.index)).to_be_visible()
        expect(self.course_max_score_text.nth(params.index)).to_have_text(
            f"Max score: {params.max_score}"
        )

        expect(self.course_min_score_text.nth(params.index)).to_be_visible()
        expect(self.course_min_score_text.nth(params.index)).to_have_text(
            f"Min score: {params.min_score}"
        )

        expect(self.course_estimated_time_text.nth(params.index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(params.index)).to_have_text(
            f"Estimated time: {params.estimated_time}"
        )

    def click_edit_course(self, index: int):
        self.course_menu_button.nth(index).click()
        expect(self.course_menu_edit_option.nth(index)).to_be_visible()
        self.course_menu_edit_option.nth(index).click()

    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()
        expect(self.course_menu_delete_option.nth(index)).to_be_visible()
        self.course_menu_delete_option.nth(index).click()
