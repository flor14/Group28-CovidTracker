from CovidTracker.get_covid_data import get_covid_data
from CovidTracker.plot_time_series import plot_ts
from pytest import raises
import pandas as pd
import pytest


def test_plot_ts():
    """
    Tests if the plot_time_series function gives the corret output.
    
    Returns
    -------
    None
        The test should pass and no asserts should be displayed.
    """
    # Generate test data
    df = get_covid_data("testing")
    test_plot = plot_ts(df, "testing", start = '2020-03-17', end = '2020-04-17')
    
    assert test_plot.encoding.x.field == 'date_testing', 'x_axis is not mapped correctly'
    assert test_plot.encoding.y.field == 'testing', 'y_axis is not mapped correctly'
    assert test_plot.mark == 'line', 'mark should be a line'
    assert test_plot.encoding.x.type == 'temporal', "x-axis has wrong data type"
    
    
def test_plot_ts_error():
    """
    Tests if the plot_time_series function raises errors correctly
    
    Returns
    -------
    None
        The test should pass and no asserts should be displayed.
    """
    with pytest.raises(TypeError):
        plot_ts(df = df, metric = 10)  
        
    with pytest.raises(TypeError):
        plot_ts(df = [1, 2, 3], metric = "testing")
    
    with pytest.raises(TypeError):
        plot_ts(df = df, metric = "testing", start = 20200201)
    
    with pytest.raises(ValueError):
        plot_ts(df = df, metric = "active_cases")
        
    with pytest.raises(ValueError):
        plot_ts(df = df, metric = "testing_info")
        
    with pytest.raises(ValueError):
        plot_ts(df = df, metric = "testing", start = '20-12-10')
    
    with pytest.raises(ValueError):
        plot_ts(df = df, metric = "testing", start = '1900-12-10')
        
    with pytest.raises(ValueError):
        plot_ts(df = df, metric = "testing", end = '2100-12-10')
        
    with pytest.raises(ValueError):
        plot_ts(df = df, metric = "testing", start = '2021-12-10', end = '2020-12-10')
        
