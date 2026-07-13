"""Checkout flow — information, overview, and complete pages."""

from __future__ import annotations

from playwright.sync_api import expect

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Actions for SauceDemo checkout steps 1 → 2 → complete."""

    # Step One — Your Information
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"

    # Step Two — Overview
    FINISH_BUTTON = "#finish"
    SUMMARY_ITEM = ".cart_item"

    # Complete
    COMPLETE_HEADER = ".complete-header"
    BACK_HOME_BUTTON = "#back-to-products"

    TITLE = ".title"

    def expect_info_step(self) -> None:
        """Assert checkout information form is shown."""
        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Your Information")
        expect(self.page).to_have_url(f"{self.base_url}/checkout-step-one.html")

    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fill buyer details on step one."""
        self.page.locator(self.FIRST_NAME).fill(first_name)
        self.page.locator(self.LAST_NAME).fill(last_name)
        self.page.locator(self.POSTAL_CODE).fill(postal_code)

    def continue_to_overview(self) -> None:
        """Submit information and go to overview."""
        self.page.locator(self.CONTINUE_BUTTON).click()

    def expect_overview_step(self) -> None:
        """Assert checkout overview is shown."""
        expect(self.page.locator(self.TITLE)).to_have_text("Checkout: Overview")
        expect(self.page).to_have_url(f"{self.base_url}/checkout-step-two.html")

    def expect_overview_item(self, product_name: str) -> None:
        """Assert a product appears on the overview."""
        expect(
            self.page.locator(self.SUMMARY_ITEM).filter(has_text=product_name)
        ).to_be_visible()

    def finish(self) -> None:
        """Place the order."""
        self.page.locator(self.FINISH_BUTTON).click()

    def expect_order_complete(self) -> None:
        """Assert the thank-you / complete page is shown."""
        expect(self.page.locator(self.COMPLETE_HEADER)).to_have_text(
            "Thank you for your order!"
        )
        expect(self.page).to_have_url(f"{self.base_url}/checkout-complete.html")

    def back_home(self) -> None:
        """Return to inventory from the complete page."""
        self.page.locator(self.BACK_HOME_BUTTON).click()
