import pandas as pd

from decimal import Decimal
from pathlib import Path


def is_equal(value1, value2):
    return Decimal(value1) == Decimal(value2)


if __name__ == "__main__":
    path = Path(".")
    sheet_name = "Sheet1"
    cell = (0, 0)
    etalon = "1"

    file_output = path / "output.txt"

    with file_output.open(mode="w") as fo:
        for p in path.iterdir():
            if any([not p.is_file(),
                    ".xl" not in p.name]):
                continue

            xl = pd.read_excel(p, sheet_name=sheet_name, header=None)

            value = xl[cell[0]][cell[1]]

            if is_equal(value, etalon):
                print(f"{etalon} is found in {p}")
                fo.write(f"{p}\n")
