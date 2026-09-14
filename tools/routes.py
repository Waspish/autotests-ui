from enum import StrEnum


class AppRoute(StrEnum):
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"
    DASHBOARD = "./#/dashboard"
    CREATE_COURSE = "./#/courses/create"
    COURSES_LIST = "./#/courses"
