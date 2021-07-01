import csv
from pathlib import Path


def convert(path: Path, path_out: Path, column: int):
    if not path_out.exists():
        path_out.mkdir()

    for p in path.iterdir():
        if any([not p.is_file(),
                ".csv" not in p.name]):
            continue
        bad_rows, good_rows = [], []
        with open(p, newline='') as csvfile:
            rows = csv.reader(csvfile, delimiter=';')
            try:
                for row in rows:
                    if row[column].strip() == "":
                        bad_rows.append(row)
                        continue
                    good_rows.append(row)
            except IndexError:
                print(f"ошибка в файле {p}")
        with open(path_out / f"good_{p.name}", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(good_rows)
        if not bad_rows:
            continue
        with open(path_out / f"bad_{p.name}", 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(bad_rows)

