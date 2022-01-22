from CovidTracker.calculate_stat_summary import calculate_stat_summary
from CovidTracker.get_covid_data import get_covid_data
import pandas as pd
import pytest


def test_calculate_stat_summary():
    """Test the calculate_stat_summary() function"""

    # data_type='cases'
    input = get_covid_data()
   
    # Test output type
    assert isinstance(calculate_stat_summary(input), pd.DataFrame)
    
    # Test output size
    assert calculate_stat_summary(input).shape == (14, 7)

    # Test output column names
    assert 'date_report' in calculate_stat_summary(input).columns
    assert 'province' in calculate_stat_summary(input).columns
    assert 'cumulative_cases' in calculate_stat_summary(input).columns
    assert 'cases' in calculate_stat_summary(input).columns

    # data_type='mortality'
    input = get_covid_data(data_type='mortality')
    
    # Test output type
    assert isinstance(calculate_stat_summary(input, data_type='mortality'), pd.DataFrame)
    
    # Test output size
    assert calculate_stat_summary(input, data_type='mortality').shape == (14, 7)

    # Test output column names
    assert 'date_death_report' in calculate_stat_summary(input, data_type='mortality').columns
    assert 'province' in calculate_stat_summary(input, data_type='mortality').columns
    assert 'cumulative_deaths' in calculate_stat_summary(input, data_type='mortality').columns
    assert 'deaths' in calculate_stat_summary(input, data_type='mortality').columns

    # data_type='recovered'
    input = get_covid_data(data_type='recovered')
    
    # Test output type
    assert isinstance(calculate_stat_summary(input, data_type='recovered'), pd.DataFrame)

    # data_type='testing'
    input = get_covid_data(data_type='testing')
    
    # Test output type
    assert isinstance(calculate_stat_summary(input, data_type='testing'), pd.DataFrame)

    # data_type='active'
    input = get_covid_data(data_type='active')
    
    # Test output type
    assert isinstance(calculate_stat_summary(input, data_type='active'), pd.DataFrame)

    # data_type='dvaccine'
    input = get_covid_data(data_type='dvaccine')
    
    # Test output type
    assert isinstance(calculate_stat_summary(input, data_type='dvaccine'), pd.DataFrame)

    # data_type='avaccine'
    input = get_covid_data(data_type='avaccine')
    
    # Test output type
    assert isinstance(calculate_stat_summary(input, data_type='avaccine'), pd.DataFrame)

    # data_type='cvaccine'
    input = get_covid_data(data_type='cvaccine')
    
    # Test output type
    assert isinstance(calculate_stat_summary(input, data_type='cvaccine'), pd.DataFrame)



    
def test_calculate_stat_summary_errors():
    """Test that calculate_stat_summary() raises the correct errors"""

    # Tests that ValueErrors are raised when arguments are of right type but inappropriate value
    with pytest.raises(TypeError):
        calculate_stat_summary('2021-12-31')
        calculate_stat_summary(100)
        calculate_stat_summary(pd.DataFrame(columns=["a", "b"]), data_type=1)        

    with pytest.raises(ValueError):
        calculate_stat_summary(pd.DataFrame(columns=["a", "b"]))
        calculate_stat_summary(pd.DataFrame({"a": [1], "b":[2]}))
        calculate_stat_summary(pd.DataFrame(columns=["a", "b"]), data_type='Newcases')