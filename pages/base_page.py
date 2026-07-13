"""Shared helpers for all page objects."""

from __future__ import annotations

from playwright.sync_api import Page, expect


class BasePage:
    """Common navigation and wait helpers used by every page."""

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def goto(self, path: str = "/") -> None:
        """Open a path under the SauceDemo base URL."""
        url = self.base_url if path in ("", "/") else f"{self.base_url}{path}"
        self.page.goto(url)

    def expect_url_contains(self, fragment: str) -> None:
        """Assert the current URL contains a path fragment (glob)."""
        expect(self.page).to_have_url(f"**/*{fragment}*")
