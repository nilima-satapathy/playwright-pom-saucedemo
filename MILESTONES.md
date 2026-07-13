# Milestones — playwright-pom-saucedemo

| Milestone | Description | Status | Date |
|-----------|-------------|--------|------|
| M1 | Install Playwright + first login test (no POM) | Done | 2026-07-13 |
| M2 | Refactor to Page Object Model | Done | 2026-07-13 |
| M3 | Cart + checkout journeys | Done | 2026-07-13 |
| M4 | Negative cases + traces on fail | Done | 2026-07-13 |
| M5 | CI workflow (headless) | Done | 2026-07-13 |
| M6 | README polish | Done | 2026-07-13 |

**Project status:** ✅ **Complete** (M1–M6 · 9 tests · CI)

## M1 notes

- Target: https://www.saucedemo.com
- Stack: Python, Pytest, Playwright, pytest-playwright
- First green login test

## M2 notes

- Page objects: base, login, inventory, cart
- Credentials/products in `utils/test_data.py`

## M3 notes

- CheckoutPage + cart/checkout journeys
- 5 journey tests (before negatives)

## M4 notes

- 4 negative login tests
- Screenshot + trace on failure (`test-results/`)
- **9 green tests** total

## M5 notes

- `.github/workflows/ci.yml` — headless Playwright on push/PR
- HTML report + Playwright artifacts uploaded

## M6 notes

- Recruiter-ready README (features, architecture, CI, interview points)
- Portfolio SVGs under `docs/assets/`
- Project marked complete
