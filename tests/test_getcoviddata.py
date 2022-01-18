from CovidTracker.get_covid_data import get_covid_data 
import pandas as pd
import pytest


def test_get_covid_data():
    assert isinstance(get_covid_data(), pd.DataFrame)
    assert len(get_covid_data('cases', date = '22-11-2021')) == 14


def test_get_covid_data_errors():
    with pytest.raises(ValueError):
        get_covid_data(date = '33-22-1997')
        get_covid_data('deaths')