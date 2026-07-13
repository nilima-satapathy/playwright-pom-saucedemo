"""Cart page — review items before checkout (used heavily in M3)."""

from __future__ import annotations

from playwright.sync_api import expect

from pages.base_page import BasePage


class CartPage(BasePage):
    """Actions and selectors for /cart.html"""

    TITLE = ".title"
    CHECKOUT_BUTTON = "#checkout"
    CART_ITEM = ".cart_item"

    def expect_loaded(self) -> None:
        """Assert the Your Cart page is visible."""
        expect(self.page.locator(self.TITLE)).to_have_text("Your Cart")
        expect(self.page).to_have_url(f"{self.base_url}/cart.html")

    def expect_item_visible(self, product_name: str) -> None:
        """Assert a product name appears in the cart."""
        expect(
            self.page.locator(self.CART_ITEM).filter(has_text=product_name)
        ).to_be_visible()

    def checkout(self) -> None:
        """Start checkout from the cart."""
        self.page.locator(self.CHECKOUT_BUTTON).click()
