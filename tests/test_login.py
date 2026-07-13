"""
Login tests — Milestone 2 uses Page Object Model.

Selectors live in pages/; tests only describe user intent.
"""

from __future__ import annotations

from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils import test_data


def test_successful_login(page: Page, base_url: str) -> None:
    """Valid credentials should land on the Products (inventory) page."""
    login = LoginPage(page, base_url)
    inventory = InventoryPage(page, base_url)

    login.open()
    login.login(test_data.STANDARD_USER, test_data.STANDARD_PASSWORD)

    inventory.expect_loaded()
