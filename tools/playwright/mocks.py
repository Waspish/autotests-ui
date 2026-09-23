import re

from playwright.sync_api import Page


def mock_static_resources(page: Page):
    page.route(
        # "**/*.{ico,png,jpg,webp,mp3,mp4,woff,woff2}" or u can do like this for playwright
        re.compile(r".*\.(?:ico|png|jpg|webp|mp3|mp4|woff|woff2)$"),
        lambda route: route.abort(),
    )
