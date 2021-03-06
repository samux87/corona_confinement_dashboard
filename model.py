# Functions to extract growth parameters
import pandas as pd
from data import (
	daily_report_data,
	time_series_date_list
)

#### MODEL PARAMETERS
ndays = 10


def recent_updates(area='US', timedelta='12 hours', sort='Confirmed', df=None):
    ascending = {
        'Province/State': True
    }
    most_recent = df[df['Country/Region'] == area]['Last Update'].max() - pd.Timedelta(timedelta)
    return df[
        (df['Country/Region'] == area) & (df['Last Update'] >= most_recent)].sort_values(
            sort, ascending=ascending.get(sort, False))

def growth_rate(
        df=None,
        area=None,
        col='Country/Region',
        do_sort=False):
    data = df[df.columns[2:]].copy()
    data = data.sort_values(list(data.columns)[-1:], ascending=False)
    rates = (data.diff(axis=1)/data)
    if area:
        rates = rates[col][area]
    return rates

def doubling_time(rates):
    from math import log
    return log(2)/rates


def last_update(area='US', column='Country/Region'):
	from data import daily_report_data
	most_recent = daily_report_data['Last Update'].max().to_pydatetime()
	return most_recent


def last_update_confinement(area='Sweden', column='nb_detected'):
    """
    @TODO: update that
    :param area:
    :param column:
    :return:
    """
    data = pd.read_csv('./data/df_confinement.tsv', sep='\t')
    return data
