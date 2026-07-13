# Playwright UI Suite — SauceDemo (POM)

UI automation suite for [SauceDemo](https://www.saucedemo.com) using **Python + Playwright + Pytest**.

[![Milestones](https://img.shields.io/badge/Milestones-M1–M2%20complete-2ea44f)](./MILESTONES.md)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Pytest-2EAD33?logo=playwright)](https://playwright.dev/python/)

| | |
|---|---|
| **Status** | In progress — **M1–M2 complete** |
| **Stack** | Playwright, Pytest, pytest-playwright, Page Object Model |
| **Target** | saucedemo.com (login → cart → checkout) |
| **Progress board** | [ai-career-journey](https://github.com/nilima-satapathy/ai-career-journey) |

---

## What’s done

| Milestone | Shipped |
|-----------|---------|
| **M1** | First login test (inline selectors) |
| **M2** | Page Object Model — selectors live in `pages/` |

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
# Headless (default)
pytest

# Watch the browser
pytest --headed
```

---

## Project layout (M2)

```
playwright-pom-saucedemo/
├── README.md
├── requirements.txt
├── pytest.ini
├── MILESTONES.md
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── conftest.py
│   └── test_login.py
└── utils/
    └── test_data.py
```

**Next (M3):** cart + checkout end-to-end journeys.
