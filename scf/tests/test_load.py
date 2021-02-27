import scf
import microdf as mdf


def equal_elements(l1, l2):
    return set(l1) == set(l2)


def test_load_multiple_years():
    YEARS = [2016, 2019]
    res = scf.load(YEARS, ["income", "networth"])
    # Should return the specified columns, plus year and wgt.
    assert equal_elements(res.columns, ["income", "networth", "wgt", "year"])
    assert equal_elements(res.year.unique().tolist(), YEARS)


def test_load_single_year():
    # Test with a single year and single column.
    res = scf.load(2016, "networth")
    # Should return the specified column, plus wgt (not year).
    assert equal_elements(res.columns, ["networth", "wgt"])


def test_load_all_columns():
    # Test with a single year and all columns.
    res = scf.load(2019)
    # Should return data with many columns (generally 300-400).
    assert res.columns.size > 100


def test_load_all_years():
    # Test with a single columns and all years.
    res = scf.load(columns="wgt")
    # Should return data with many rows and two columns.
    assert res.size > 0
    assert equal_elements(res.columns, ["year", "wgt"])


def test_load_microdf():
    res = scf.load(2019, "networth", as_microdataframe=True)
    assert isinstance(res, mdf.MicroDataFrame)
