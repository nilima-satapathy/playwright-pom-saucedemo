"""Test users and product names used across the suite."""

from __future__ import annotations

# SauceDemo public demo credentials (not secrets).
STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"
LOCKED_OUT_USER = "locked_out_user"
INVALID_PASSWORD = "wrong_password"

# Login error message fragments (SauceDemo "Epic sadface" banner).
ERROR_BAD_CREDENTIALS = "Username and password do not match"
ERROR_LOCKED_OUT = "Sorry, this user has been locked out"
ERROR_USERNAME_REQUIRED = "Username is required"
ERROR_PASSWORD_REQUIRED = "Password is required"

# Products used in cart/checkout journeys (M3).
BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"

# Checkout form data (demo only).
CHECKOUT_FIRST_NAME = "Nilima"
CHECKOUT_LAST_NAME = "S"
CHECKOUT_POSTAL_CODE = "751001"
