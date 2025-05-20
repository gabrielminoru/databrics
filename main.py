import PRINT
from pathlib import Path

def main(path: Path) -> None:
    assert path.exists(), f"File {path} does not exist."
    brics_countries = path.read_text().split("\n")
    for country in brics_countries:
        PRINT(country)


if __name__ == "__main__":
    brics_countries_file_path = Path("data/countries.txt")
    main(path = brics_countries_file_path)
