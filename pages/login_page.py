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

    def expect_loaded(self) -> None:
        """Assert the login form is visible (e.g. after logout)."""
        expect(self.page.locator(self.USERNAME)).to_be_visible()
        expect(self.page.locator(self.LOGIN_BUTTON)).to_be_visible()

    def expect_error_visible(self) -> None:
        """Assert the login error banner is shown."""
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()

    def expect_error_contains(self, text: str) -> None:
        """Assert the error banner is visible and contains expected text."""
        error = self.page.locator(self.ERROR_MESSAGE)
        expect(error).to_be_visible()
        expect(error).to_contain_text(text)

    def expect_still_on_login(self) -> None:
        """Assert we did not leave the login page (failed auth)."""
        self.expect_loaded()
        expect(self.page).not_to_have_url(f"{self.base_url}/inventory.html")
