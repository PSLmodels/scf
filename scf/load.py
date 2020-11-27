import microdf as mdf
import pandas as pd


VALID_YEARS = [
    1989,
    1992,
    1995,
    1998,
    2001,
    2004,
    2007,
    2010,
    2013,
    2016,
    2019,
]


def scf_url(year: int):
    """ Returns the URL of the SCF summary microdata zip file for a year.

    :param year: Year of SCF summary microdata to retrieve.
    :type year: int
    :return: URL of summary microdata zip file for the given year.
    :rtype: str
    """
    assert year in VALID_YEARS, "The SCF is not available for " + str(year)
    return (
        "https://www.federalreserve.gov/econres/files/scfp"
        + str(year)
        + "s.zip"
    )


def load_single_scf(year: int, columns: list):
    """ Loads SCF summary microdata for a given year and set of columns.

    :param year: Year of SCF summary microdata to retrieve.
    :type year: int
    :param columns: List of columns. The weight column `wgt` is always
        returned. Defaults to all columns in the summary dataset.
    :type columns: list
    :return: SCF summary microdata for the given year.
    :rtype: pd.DataFrame
    """
    # Add wgt to all returns.
    if columns is not None:
        columns = list(set(columns) | set(["wgt"]))
    return mdf.read_stata_zip(scf_url(year), columns=columns)


def load(years: list = VALID_YEARS, columns: list = None):
    """ Loads SCF summary microdata for a set of years and columns.

    :param years: Year(s) to load SCF data for. Can be a list or single number.
        Defaults to all available years, starting with 1989.
    :type years: list
    :param columns: List of columns. The weight column `wgt` is always
        returned. Defaults to all columns in the summary dataset.
    :type columns: list
    :return: SCF summary microdata for the set of years.
    :rtype: pd.DataFrame
    """
    # Make cols a list if a single column is passed.
    if columns is not None:
        columns = mdf.listify(columns)
    # If years is a single year rather than a list, return without a loop.
    if isinstance(years, int):
        return load_single_scf(years, columns)
    # Otherwise append to a list within a loop, and return concatenation.
    scfs = []
    for year in years:
        tmp = load_single_scf(year, columns)
        tmp["year"] = year
        scfs.append(tmp)
    return pd.concat(scfs)
