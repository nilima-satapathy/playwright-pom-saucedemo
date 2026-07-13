# Playwright UI Suite — SauceDemo (POM)

UI automation suite for [SauceDemo](https://www.saucedemo.com) using **Python + Playwright + Pytest**.

[![CI](https://github.com/nilima-satapathy/playwright-pom-saucedemo/actions/workflows/ci.yml/badge.svg)](https://github.com/nilima-satapathy/playwright-pom-saucedemo/actions/workflows/ci.yml)
[![Milestones](https://img.shields.io/badge/Milestones-M1–M5%20complete-2ea44f)](./MILESTONES.md)
[![Tests](https://img.shields.io/badge/Tests-9%20passed-success)](./tests)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Pytest-2EAD33?logo=playwright)](https://playwright.dev/python/)

| | |
|---|---|
| **Status** | In progress — **M1–M5 complete** |
| **Stack** | Playwright, Pytest, pytest-playwright, Page Object Model, GitHub Actions |
| **Target** | saucedemo.com (login → cart → checkout → logout) |
| **Tests** | **9** (5 happy-path + 4 negative) |
| **CI** | Headless Chromium on every push/PR · [Actions](https://github.com/nilima-satapathy/playwright-pom-saucedemo/actions) |
| **On failure** | Screenshot + Playwright trace → `test-results/` (uploaded as CI artifact) |
| **Progress board** | [ai-career-journey](https://github.com/nilima-satapathy/ai-career-journey) |

---

## What’s done

| Milestone | Shipped |
|-----------|---------|
| **M1** | First login test |
| **M2** | Page Object Model (`pages/`) |
| **M3** | Cart + checkout journeys |
| **M4** | Negative login + screenshot/trace on fail |
| **M5** | GitHub Actions headless CI + report/trace artifacts |

---

## Journeys covered

**Happy path**

1. Login → Products  
2. Add single item → cart  
3. Add two items → cart  
4. Full checkout → thank-you  
5. Checkout → logout  

**Negative login**

6. Wrong password → error banner  
7. Locked-out user → locked message  
8. Missing username → required error  
9. Missing password → required error  

---

## Setup (Windows / PowerShell)

```powershell
cd Desktop\Code\playwright-pom-saucedemo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

## Run tests

```powershell
# Headless (default) — same mode as CI
pytest

# Watch the browser
pytest --headed

# With HTML report
mkdir reports -Force
pytest --html=reports/report.html --self-contained-html
```

### Failure artifacts (M4 + M5)

On a failed test, Playwright writes under `test-results/`:

- screenshot (PNG)
- **trace** (ZIP) — full step replay

```powershell
playwright show-trace test-results\<folder>\trace.zip
```

On CI, download **pytest-html-report** and **playwright-test-results** from the Actions run.

---

## Project layout (M5)

```
playwright-pom-saucedemo/
├── .github/workflows/ci.yml
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_negative.py
└── utils/
    └── test_data.py
```

**Next (M6):** README polish + portfolio screenshot/GIF.
