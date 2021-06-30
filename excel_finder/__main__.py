import pandas as pd

from decimal import Decimal
from pathlib import Path


if __name__ == "__main__":
    path = Path("..")
    column = 9
    file_output = path / "output.txt"

    for p in path.iterdir():
        if any([not p.is_file(),
                ".csv" not in p.name]):
            continue

        df = pd.read_csv(p, header=None)
        rows = []
        for i, value in enumerate(df[column]):
            if not value:
                rows.append(df[i])
                df.drop([i,], axis=0)

        print(value)
        with file_output.open(mode="w") as fo:
        # if is_equal(value, etalon):
            #     print(f"{etalon} is found in {p}")
            #     fo.write(f"{p}\n")
