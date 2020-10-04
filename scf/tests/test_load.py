import scf


def equal_elements(l1, l2):
    return set(l1) == set(l2)

def test_load():
    YEARS = [2016, 2019]
    res = scf.load(YEARS, ['income', 'networth'])
    # Should return the specified columns, plus year and wgt.
    assert equal_elements(res.columns, ['income', 'networth', 'wgt', 'year'])
    assert equal_elements(res.year.unique().tolist(), YEARS)
