import pandas as pd

def calculate_stat_summary(df):
    """Creates summary information about the 
       covid cases in each province of Canada

    Parameters
    ----------
    df : pandas.DataFrame
        Pandas DataFrame containing covid data to summary.

    Returns
    -------
    pandas.DataFrame
        pandas DataFrame containing summary information.

    Examples
    --------
    >>> calculate_stat_summary(covid_df)
    """

    # Check input parameter validity
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Invalid argument type: df must be a pandas DataFrame")
    elif len(df) == 0:
        raise ValueError("Argument value error: df must contain at least one row of data")
    elif not (('date_report' in df.columns) and ('province' in df.columns)):
        raise ValueError("Argument value error: df must contain date_report and province columns")

    df['date_report'] = pd.to_datetime(df['date_report'], format='%d-%m-%Y')
    max_date = df.loc[df['date_report'].argmax(), 'date_report']
    columns = ['date_report', 'province'] + list(set(df.columns) - set(['date_report', 'province']))
    summary = df[df['date_report'] == max_date][columns].sort_values('province')
    return summary
