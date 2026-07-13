"""
Journeys: cart → checkout → complete order (+ logout).

Milestone 3 — full purchase path using Page Objects.
"""

from __future__ import annotations

from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils import test_data


def test_checkout_completes_order(page: Page, base_url: str) -> None:
    """Login → add backpack → checkout info → finish → thank-you page."""
    login = LoginPage(page, base_url)
    inventory = InventoryPage(page, base_url)
    cart = CartPage(page, base_url)
    checkout = CheckoutPage(page, base_url)

    login.open()
    login.login(test_data.STANDARD_USER, test_data.STANDARD_PASSWORD)
    inventory.expect_loaded()

    inventory.add_to_cart_by_name(test_data.BACKPACK)
    inventory.open_cart()
    cart.expect_loaded()
    cart.expect_item_visible(test_data.BACKPACK)
    cart.checkout()

    checkout.expect_info_step()
    checkout.fill_info(
        test_data.CHECKOUT_FIRST_NAME,
        test_data.CHECKOUT_LAST_NAME,
        test_data.CHECKOUT_POSTAL_CODE,
    )
    checkout.continue_to_overview()

    checkout.expect_overview_step()
    checkout.expect_overview_item(test_data.BACKPACK)
    checkout.finish()

    checkout.expect_order_complete()


def test_checkout_then_logout(page: Page, base_url: str) -> None:
    """Full purchase, return to products, then logout back to login page."""
    login = LoginPage(page, base_url)
    inventory = InventoryPage(page, base_url)
    cart = CartPage(page, base_url)
    checkout = CheckoutPage(page, base_url)

    login.open()
    login.login(test_data.STANDARD_USER, test_data.STANDARD_PASSWORD)
    inventory.expect_loaded()

    inventory.add_to_cart_by_name(test_data.BIKE_LIGHT)
    inventory.open_cart()
    cart.checkout()

    checkout.fill_info(
        test_data.CHECKOUT_FIRST_NAME,
        test_data.CHECKOUT_LAST_NAME,
        test_data.CHECKOUT_POSTAL_CODE,
    )
    checkout.continue_to_overview()
    checkout.finish()
    checkout.expect_order_complete()

    checkout.back_home()
    inventory.expect_loaded()
    inventory.logout()
    login.expect_loaded()
