def get_covid_data(type, loc, date):
    """Acquires Canada Covid Data within specified
    search range

    Parameters
    ----------
    type : str, optional
        Type of data to be returned 

    loc : str, optional
        Location (province) filter for the data 

    date : str, optional
        Date to search, specified as DD-MM-YYYY
    

    Examples
    --------
    >>> get_covid_data('cases', 'BC', '13-01-2021')
    >>> get_covid_data()

    """