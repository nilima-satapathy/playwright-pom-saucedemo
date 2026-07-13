"""
Journey: login → add product(s) → cart.

Milestone 3 — cart coverage using Page Objects.
"""

from __future__ import annotations

from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils import test_data


def _login(page: Page, base_url: str) -> InventoryPage:
    login = LoginPage(page, base_url)
    inventory = InventoryPage(page, base_url)
    login.open()
    login.login(test_data.STANDARD_USER, test_data.STANDARD_PASSWORD)
    inventory.expect_loaded()
    return inventory


def test_add_single_item_to_cart(page: Page, base_url: str) -> None:
    """User can add one product and see it in the cart."""
    inventory = _login(page, base_url)
    cart = CartPage(page, base_url)

    inventory.add_to_cart_by_name(test_data.BACKPACK)
    inventory.expect_cart_badge_count(1)
    inventory.open_cart()

    cart.expect_loaded()
    cart.expect_item_visible(test_data.BACKPACK)


def test_add_two_items_to_cart(page: Page, base_url: str) -> None:
    """User can add multiple products; badge and cart list stay correct."""
    inventory = _login(page, base_url)
    cart = CartPage(page, base_url)

    inventory.add_to_cart_by_name(test_data.BACKPACK)
    inventory.add_to_cart_by_name(test_data.BIKE_LIGHT)
    inventory.expect_cart_badge_count(2)
    inventory.open_cart()

    cart.expect_loaded()
    cart.expect_item_visible(test_data.BACKPACK)
    cart.expect_item_visible(test_data.BIKE_LIGHT)
