"""
Negative login cases — Milestone 4.

Validates error handling when authentication should fail.
"""

from __future__ import annotations

from playwright.sync_api import Page

from pages.login_page import LoginPage
from utils import test_data


def test_login_with_wrong_password(page: Page, base_url: str) -> None:
    """Invalid password shows credentials error and stays on login."""
    login = LoginPage(page, base_url)

    login.open()
    login.login(test_data.STANDARD_USER, test_data.INVALID_PASSWORD)

    login.expect_error_contains(test_data.ERROR_BAD_CREDENTIALS)
    login.expect_still_on_login()


def test_login_locked_out_user(page: Page, base_url: str) -> None:
    """Locked-out user cannot enter the store."""
    login = LoginPage(page, base_url)

    login.open()
    login.login(test_data.LOCKED_OUT_USER, test_data.STANDARD_PASSWORD)

    login.expect_error_contains(test_data.ERROR_LOCKED_OUT)
    login.expect_still_on_login()


def test_login_missing_username(page: Page, base_url: str) -> None:
    """Empty username shows a required-field error."""
    login = LoginPage(page, base_url)

    login.open()
    login.login("", test_data.STANDARD_PASSWORD)

    login.expect_error_contains(test_data.ERROR_USERNAME_REQUIRED)
    login.expect_still_on_login()


def test_login_missing_password(page: Page, base_url: str) -> None:
    """Empty password shows a required-field error."""
    login = LoginPage(page, base_url)

    login.open()
    login.login(test_data.STANDARD_USER, "")

    login.expect_error_contains(test_data.ERROR_PASSWORD_REQUIRED)
    login.expect_still_on_login()
