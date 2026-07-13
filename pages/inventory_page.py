"""Inventory (Products) page — shown after a successful login."""

from __future__ import annotations

from playwright.sync_api import expect

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Actions and selectors for /inventory.html"""

    TITLE = ".title"
    CART_LINK = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"

    def expect_loaded(self) -> None:
        """Assert we landed on the Products inventory page."""
        expect(self.page.locator(self.TITLE)).to_have_text("Products")
        expect(self.page).to_have_url(f"{self.base_url}/inventory.html")

    def add_to_cart_by_name(self, product_name: str) -> None:
        """
        Add a product by its display name (used from M3).

        SauceDemo buttons sit inside the inventory item card that contains
        the product title.
        """
        item = self.page.locator(".inventory_item").filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def open_cart(self) -> None:
        """Open the shopping cart from the header icon."""
        self.page.locator(self.CART_LINK).click()
