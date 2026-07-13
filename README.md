# Playwright UI Suite — SauceDemo (POM)

UI automation suite for [SauceDemo](https://www.saucedemo.com) using **Python + Playwright + Pytest**.

[![Milestones](https://img.shields.io/badge/Milestones-M1–M3%20complete-2ea44f)](./MILESTONES.md)
[![Tests](https://img.shields.io/badge/Tests-5%20passed-success)](./tests)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Pytest-2EAD33?logo=playwright)](https://playwright.dev/python/)

| | |
|---|---|
| **Status** | In progress — **M1–M3 complete** |
| **Stack** | Playwright, Pytest, pytest-playwright, Page Object Model |
| **Target** | saucedemo.com (login → cart → checkout → logout) |
| **Tests** | **5** end-to-end journeys (all green) |
| **Progress board** | [ai-career-journey](https://github.com/nilima-satapathy/ai-career-journey) |

---

## What’s done

| Milestone | Shipped |
|-----------|---------|
| **M1** | First login test |
| **M2** | Page Object Model (`pages/`) |
| **M3** | Cart + checkout journeys (5 tests) |

---

## Journeys covered

1. **Login** — valid user lands on Products  
2. **Single item cart** — add backpack → cart badge + line item  
3. **Multi-item cart** — backpack + bike light  
4. **Checkout** — info → overview → “Thank you for your order!”  
5. **Checkout + logout** — complete order → back home → logout  

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
pytest
pytest --headed   # watch the browser
```

---

## Project layout (M3)

```
playwright-pom-saucedemo/
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
│   └── test_checkout.py
└── utils/
    └── test_data.py
```

**Next (M4):** negative login + screenshot/trace on failure.
