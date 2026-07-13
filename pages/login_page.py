"""Login page — SauceDemo entry screen."""

from __future__ import annotations

from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Actions and selectors for https://www.saucedemo.com/"""

    # Selectors live here once — tests never hard-code them.
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def open(self) -> None:
        """Navigate to the login page."""
        self.goto("/")

    def login(self, username: str, password: str) -> None:
        """Fill credentials and submit the login form."""
        self.page.locator(self.USERNAME).fill(username)
        self.page.locator(self.PASSWORD).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()

    def expect_error_visible(self) -> None:
        """Assert the login error banner is shown (used from M4)."""
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()
