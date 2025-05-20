from pathlib import Path

data = Path("data/countries.txt").read_text()

def test_brasil_is_from_brics():
    assert "Brasil" in data

def test_russia_is_from_brics():
    assert "Russia" in data

def test_india_is_from_brics():
    assert "India" in data

def test_china_is_from_brics():
    assert "China" in data

def test_south_africa_is_from_brics():
    assert "South Africa" in data

def test_usa_is_not_from_brics():
    assert "United States of America" not in data
