# Milestones — playwright-pom-saucedemo

| Milestone | Description | Status | Date |
|-----------|-------------|--------|------|
| M1 | Install Playwright + first login test (no POM) | Done | 2026-07-13 |
| M2 | Refactor to Page Object Model | Done | 2026-07-13 |
| M3 | Cart + checkout journeys | Done | 2026-07-13 |
| M4 | Negative cases + traces on fail | Done | 2026-07-13 |
| M5 | CI workflow (headless) | Done | 2026-07-13 |
| M6 | README polish | Pending | — |

## M1 notes

- Target: https://www.saucedemo.com
- Stack: Python, Pytest, Playwright, pytest-playwright
- First green login test

## M2 notes

- Page objects: base, login, inventory, cart
- Credentials/products in `utils/test_data.py`

## M3 notes

- CheckoutPage + 5 journey tests

## M4 notes

- 4 negative login tests
- Screenshot + trace on failure (`test-results/`)
- **9 green tests** total

## M5 notes

- `.github/workflows/ci.yml` — headless Playwright on push/PR
- Installs Chromium with OS deps on Ubuntu
- Uploads HTML report + Playwright `test-results/` artifacts
- `pytest-html` added to requirements
