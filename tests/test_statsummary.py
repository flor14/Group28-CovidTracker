from CovidTracker.calculate_stat_summary import calculate_stat_summary
from CovidTracker.get_covid_data import get_covid_data
import pandas as pd
import pytest


def test_calculate_stat_summary():
    """Test the calculate_stat_summary() function"""

    input = get_covid_data()
   
    # Test output type
    assert isinstance(calculate_stat_summary(input), pd.DataFrame)
    
    # Test output size
    assert calculate_stat_summary(input).shape == (14, 4)

    # Test output column names
    assert 'date_report' in calculate_stat_summary(input).columns
    assert 'province' in calculate_stat_summary(input).columns
    assert 'cumulative_cases' in calculate_stat_summary(input).columns
    assert 'cases' in calculate_stat_summary(input).columns
    
def test_calculate_stat_summary_errors():
    """Test that calculate_stat_summary() raises the correct errors"""

    # Tests that ValueErrors are raised when arguments are of right type but inappropriate value
    with pytest.raises(TypeError):
        calculate_stat_summary('2021-12-31')
        calculate_stat_summary(100)
        calculate_stat_summary()

    with pytest.raises(ValueError):
        calculate_stat_summary(pd.DataFrame(columns=["a", "b"]))
        calculate_stat_summary(pd.DataFrame({"a": [1], "b":[2]}))