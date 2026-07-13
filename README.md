# Playwright UI Suite — SauceDemo (POM)

UI automation suite for [SauceDemo](https://www.saucedemo.com) using **Python + Playwright + Pytest**.

[![Milestones](https://img.shields.io/badge/Milestones-M1%20complete-2ea44f)](./MILESTONES.md)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Pytest-2EAD33?logo=playwright)](https://playwright.dev/python/)

| | |
|---|---|
| **Status** | In progress — **M1 complete** |
| **Stack** | Playwright, Pytest, pytest-playwright |
| **Target** | saucedemo.com (login → cart → checkout) |
| **Progress board** | [ai-career-journey](https://github.com/nilima-satapathy/ai-career-journey) |

---

## Milestone 1 (done)

Working login test against SauceDemo. **No Page Object Model yet** (that is M2).

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

## Project layout (M1)

```
playwright-pom-saucedemo/
├── README.md
├── requirements.txt
├── pytest.ini
├── MILESTONES.md
└── tests/
    ├── conftest.py      # base_url fixture
    └── test_login.py    # first login test (inline selectors)
```

Full POM structure lands in **M2**.
