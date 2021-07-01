from pathlib import Path

from excel_finder.convert import convert


def test_smoke():
    p_in = Path(__file__).parent
    p_out = Path(__file__).parent / "output"
    convert(p_in, p_out, 1)

    bad_text = (p_out / "bad_dataframe.csv").read_text()
    good_text = (p_out / "good_dataframe.csv").read_text()

    assert bad_text == """1;;3;4;5
1;;3;4;5
"""
    assert good_text == """1;2;3;4;5
1;2;3;4;5
1;2;3;4;5
1;2;3;4;5
"""
