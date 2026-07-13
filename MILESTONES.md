# Milestones — playwright-pom-saucedemo

| Milestone | Description | Status | Date |
|-----------|-------------|--------|------|
| M1 | Install Playwright + first login test (no POM) | Done | 2026-07-13 |
| M2 | Refactor to Page Object Model | Done | 2026-07-13 |
| M3 | Cart + checkout journeys | Pending | — |
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
- Cart/inventory helpers ready for M3 journeys
