# coding=utf-8
"""Test scenarios."""

import pytest
from pytest_bdd import scenarios


pytestmark = [
    pytest.mark.vcr,
    pytest.mark.usefixtures("ddspan"),
]

scenarios("features")
