# PyOpenFisheries
[![PyPI version](https://badge.fury.io/py/pyopenfisheries.svg)](https://badge.fury.io/py/pyopenfisheries)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

PyOpenFisheries makes it even easier to access the [OpenFisheries API](https://github.com/OpenFisheries/api.openfisheries.org) in Python.

A good usecase of this library is to gather data to plot in a Jupyter Notebook, or to collect data to run time-series analysis on.

![Screenshot](Sphinx-docs/example.png)


Learn more about [OpenFisheries.org](openfisheries.org).

Here is a [List of ASFIS codes with species names](https://www.iccat.int/Documents/SCRS/Manual/Appendices/Appendix_5_1_Bycatch_SpeciesList.pdf).

#### this package depends on [Requests](https://pypi.org/project/requests/).


# Documentation
## pyopenfisheries.pyopenfisheries module


### class pyopenfisheries.pyopenfisheries.PyOpenFisheries(\*\*kwargs)
Bases: `object`

Base class for accessing the OpenFisheries API.
Useful for gathering data for plots or analysis.

Returns:

    instance: base OpenFisheries API wrapper

Examples:


    >>> open_fish_conn = PyOpenFisheries()
    >>> skipjack_tuna = open_fish_conn.annual_landings(species="SKJ").filter_years(start_year=1970,end_year=1991)
    >>> print(skipjack_tuna.landings)
    [{'year': 1970, 'catch': 402166}...{'year': 1991, 'catch': 1575170}]
    >>> print(skipjack_tuna.summarize())
    Landings of SKJ globally from 1970 to 1991


Attributes:

    landings: List of dictionaries containing the year and landing count.
    species: if present - three-letter ASFIS species code (i.e. “SKJ” - Skipjack Tuna).
    country: if present - ISO-3166 alpha 3 country code (i.e. “USA” - United States).
    start_year: if present - start year of filtered landings data.
    end_year : if present - end year of filtered landings data.


#### annual_landings(species=None, country=None)
Gathers annual fishery landings filtered by either species or
country. If neither fish nor country are specified, then this
will return global aggregate landings data.

Args:

    species: three-letter ASFIS species code (i.e. “SKJ” - Skipjack Tuna)
    country: ISO-3166 alpha 3 country code (i.e. “USA” - United States)

Returns:

    instance: PyOpenFisheries instance with landings populated


#### filter_years(start_year=1950, end_year=2018)
Filters annual fishing data to within a time-frame.

Args:

    start_year: 4 digit integer year (i.e. 1980)
    end_year: 4 digit integer year (i.e. 2015)

Returns:

    instance: PyOpenFisheries instance with years filtered.


#### summarize()
Summarizes what has been returned from OpenFisheries.

#### label()
Useful as a legend / for plots.


