# Milestones — playwright-pom-saucedemo

| Milestone | Description | Status | Date |
|-----------|-------------|--------|------|
| M1 | Install Playwright + first login test (no POM) | Done | 2026-07-13 |
| M2 | Refactor to Page Object Model | Done | 2026-07-13 |
| M3 | Cart + checkout journeys | Done | 2026-07-13 |
| M4 | Negative cases + traces on fail | Pending | — |
| M5 | CI workflow (headless) | Pending | — |
| M6 | README polish | Pending | — |

## M1 notes

- Target: https://www.saucedemo.com
- Stack: Python, Pytest, Playwright, pytest-playwright
- One green test: successful login with `standard_user` / `secret_sauce`
- No POM yet — selectors were inline in `tests/test_login.py`

## M2 notes

- Page objects: `base_page`, `login_page`, `inventory_page`, `cart_page`
- Credentials/products in `utils/test_data.py`
- Login test uses POM only (no raw selectors in tests)

## M3 notes

- Added `checkout_page.py` (info → overview → complete)
- **5 green tests** covering ≥3 user journeys:
  1. Successful login
  2. Add single item to cart
  3. Add two items to cart
  4. Full checkout to thank-you page
  5. Checkout then logout back to login
