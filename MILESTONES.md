# Milestones — playwright-pom-saucedemo

| Milestone | Description | Status | Date |
|-----------|-------------|--------|------|
| M1 | Install Playwright + first login test (no POM) | Done | 2026-07-13 |
| M2 | Refactor to Page Object Model | Pending | — |
| M3 | Cart + checkout journeys | Pending | — |
| M4 | Negative cases + traces on fail | Pending | — |
| M5 | CI workflow (headless) | Pending | — |
| M6 | README polish | Pending | — |

## M1 notes

- Target: https://www.saucedemo.com
- Stack: Python, Pytest, Playwright, pytest-playwright
- One green test: successful login with `standard_user` / `secret_sauce`
- No POM yet — selectors are inline in `tests/test_login.py`
