"""
Shared Pytest setup for Playwright UI tests.

- base_url fixture for all page objects
- Browser/page fixtures come from pytest-playwright
- Failure artifacts (screenshot + trace) configured in pytest.ini (M4)
"""

from __future__ import annotations

import os

import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    """SauceDemo root. Override with SAUCEDEMO_BASE_URL if needed."""
    return os.getenv("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com")
