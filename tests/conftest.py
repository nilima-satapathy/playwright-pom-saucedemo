"""
Shared Pytest setup for Playwright UI tests.

Milestone 1: base URL fixture only.
Browser/page fixtures come from pytest-playwright.
"""

from __future__ import annotations

import os

import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    """SauceDemo root. Override with SAUCEDEMO_BASE_URL if needed."""
    return os.getenv("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com")
