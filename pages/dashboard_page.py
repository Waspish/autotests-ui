from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = self.page.get_by_test_id("dashboard-toolbar-title-text")

        self.students_title = self.page.get_by_test_id("students-widget-title-text")
        self.students_chart = self.page.get_by_test_id("students-bar-chart")

        self.activities_title = self.page.get_by_test_id("activities-widget-title-text")
        self.activities_chart = self.page.get_by_test_id("activities-line-chart")

        self.courses_title = self.page.get_by_test_id("courses-widget-title-text")
        self.courses_chart = self.page.get_by_test_id("courses-pie-chart")

        self.scores_title = self.page.get_by_test_id("scores-widget-title-text")
        self.scores_chart = self.page.get_by_test_id("scores-scatter-chart")

    def verify_dashboard_title_displayed_correctly(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("Dashboard")

    def verify_students_chart_and_title_displayed_correctly(self):
        expect(self.students_title).to_be_visible()
        expect(self.students_title).to_have_text("Students")
        expect(self.students_chart).to_be_visible()

    def verify_activities_chart_and_title_displayed_correctly(self):
        expect(self.activities_title).to_be_visible()
        expect(self.activities_title).to_have_text("Activities")
        expect(self.activities_chart).to_be_visible()

    def verify_courses_chart_and_title_displayed_correctly(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text("Courses")
        expect(self.courses_chart).to_be_visible()

    def verify_scores_chart_and_title_displayed_correctly(self):
        expect(self.scores_title).to_be_visible()
        expect(self.scores_title).to_have_text("Scores")
        expect(self.scores_chart).to_be_visible()
