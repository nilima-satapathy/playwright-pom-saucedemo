# Milestones — playwright-pom-saucedemo

| Milestone | Description | Status | Date |
|-----------|-------------|--------|------|
| M1 | Install Playwright + first login test (no POM) | Done | 2026-07-13 |
| M2 | Refactor to Page Object Model | Done | 2026-07-13 |
| M3 | Cart + checkout journeys | Done | 2026-07-13 |
| M4 | Negative cases + traces on fail | Done | 2026-07-13 |
| M5 | CI workflow (headless) | Pending | — |
| M6 | README polish | Pending | — |

## M1 notes

- Target: https://www.saucedemo.com
- Stack: Python, Pytest, Playwright, pytest-playwright
- One green test: successful login with `standard_user` / `secret_sauce`

## M2 notes

- Page objects: `base_page`, `login_page`, `inventory_page`, `cart_page`
- Credentials/products in `utils/test_data.py`

## M3 notes

- Added `checkout_page.py` (info → overview → complete)
- 5 green journey tests (login / cart / checkout / logout)

## M4 notes

- Negative login suite (`tests/test_negative.py`):
  - wrong password
  - locked-out user
  - missing username
  - missing password
- `pytest.ini`: `--screenshot=only-on-failure` + `--tracing=retain-on-failure`
- Artifacts written to `test-results/` (gitignored)
- View trace: `playwright show-trace test-results/.../trace.zip`
- **9 green tests** total
