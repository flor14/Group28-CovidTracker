# CovidTracker

Provides basic data cleaning, wrangling and plotting of Covid tracking data

## Features 
The CovidTracker package is designed for the easy retrieval and analysis of data pertaining to Covid trends in Canada, including information about cases, vaccinations and testing. The package serves as a wrapper for the opencovid.ca API, and provides additional helper functions for visualising the data, either as a time series or in the form of a map. 

`get_covid_data()`: Retrieve cleaned and formatted data of specified type and within (optionally) provided time ranges and locations
`plot_time_series()`: Function for plotting time series trends in Covid data, including options for trendlines and smoothing
`calculate_stat_summary()`: Function for returning key statistical information about Covid data, such as long run trends and comparisons between provinces
`plot_geographical()`: Function for plotting chloropleth maps with Covid data 

## Installation

```bash
$ pip install CovidTracker
```

## Usage

- TODO

## Contributing

We welcome and recognize all contributions. Please see contributing guidelines in the Contributing document. This repository is currently maintained by

* Cuthbert Chow (@cuthchow)
* Tianwei Wang (@Davidwang11)
* Siqi Tao (@SiqiTao)
* Jessie Wong (@jessie14)

## License

`CovidTracker` was created by Group 28. It is licensed under the terms of the MIT license.

## Credits

`CovidTracker` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
