import pytest
from cat_facts import fetch_cat_fact

def test_fetch_cat_fact_returns_valid_status_code():
    status_code, _ = fetch_cat_fact()
    assert status_code == 200

def test_fetch_cat_fact_returns_fact_data():
    _, data = fetch_cat_fact()
    assert "fact" in data

