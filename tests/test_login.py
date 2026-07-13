"""
Milestone 1 — first login test (no Page Object Model yet).

Selectors live in the test on purpose; M2 will move them into pages/.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect


def test_successful_login(page: Page, base_url: str) -> None:
    """Valid credentials should land on the Products (inventory) page."""
    page.goto(base_url)

    # SauceDemo login form
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # After login, inventory header shows "Products"
    expect(page.locator(".title")).to_have_text("Products")
    expect(page).to_have_url(f"{base_url.rstrip('/')}/inventory.html")
