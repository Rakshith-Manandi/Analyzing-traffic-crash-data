import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt


def read_accidents(filename):
    '''
    This function reads accident data and returns pre-processed data.
 
    :param filename: input filename string
    :type filename: string

    :returns: pre-processed data for plotting
    :return type: pandas dataframe
    '''
    assert isinstance(filename,str)

    traffic_data = pd.read_csv(filename,
                               usecols=[0, 1, 11, 12, 13, 25, 26, 50, 51])
    traffic_data = traffic_data.rename(
        columns={'ST_CASE':'case_id', 'LONGITUD':'longitude',
                 'DRUNK_DR':'drunk_drivers', 'FATALS':'fatalities'})
    traffic_data.columns = traffic_data.columns.str.lower()
    traffic_data['date'] = pd.to_datetime(traffic_data[['day', 'month', 'year']])
    traffic_data = traffic_data[['case_id', 'date', 'state', 'latitude', 'longitude',
                                 'drunk_drivers', 'fatalities']].sort_values('date')

    assert isinstance(traffic_data,pd.DataFrame)
    return traffic_data

def sum_columns_by_groups_over_time(data, start_date, end_date, grouping, column):
    '''
    This function returns a date interval as an x axis variable, and sums columns by groups and
    returns it as y-axis variable.
 
    :param data: input dataframe
    :type data: pandas dataframe
    :param start_date: start of date interval
    :type start_date: string
    :param end_date: end of date interval
    :type end_date: string
    :param grouping: grouping
    :type grouping: string
    :param column: column to sum over
    :type column: string

    :returns: dates np array, sum np array
    :return type: 2-tuple of np arrays
    '''
    assert isinstance(data,pd.DataFrame)
    assert isinstance(start_date, str)
    assert isinstance(end_date, str)
    assert isinstance(grouping, str)
    assert isinstance(column, str)
    traffic_per_date = np.asarray(data.groupby(grouping)[column].sum())
    traffic_dates = np.arange(start_date, end_date, dtype='datetime64[D]')

    assert isinstance(traffic_per_date,np.ndarray)
    assert isinstance(traffic_dates,np.ndarray)

    return traffic_dates, traffic_per_date

def sum_columns_by_groups_over_time_monthly_mean(data, start_date, end_date, grouping, column):
    '''
    This function returns a date interval as an x axis variable, and sums columns by groups and
    returns the 30-day mean as y-axis variable.
 
    :param data: input dataframe
    :type data: pandas dataframe
    :param start_date: start of date interval
    :type start_date: string
    :param end_date: end of date interval
    :type end_date: string
    :param grouping: grouping
    :type grouping: string
    :param column: column to sum over
    :type column: string

    :returns: dates np array, sum np array
    :return type: 2-tuple of np arrays
    '''
    assert isinstance(data,pd.DataFrame)
    assert isinstance(start_date, str)
    assert isinstance(end_date, str)
    assert isinstance(grouping, str)
    assert isinstance(column, str)
    traffic_dates, traffic_per_date = sum_columns_by_groups_over_time(data, start_date, end_date, grouping, column)

    # thirty day moving average of traffic fatalites by date
    traffic_average = pd.Series(traffic_per_date).rolling(window=30).mean()
    traffic_average = np.asarray(traffic_average.drop(traffic_average.index[:29]))
    traffic_average = np.round(traffic_average, 0)

    traffic_range = traffic_dates[15:351]
    assert isinstance(traffic_per_date,np.ndarray)
    assert isinstance(traffic_dates,np.ndarray)
    return traffic_range, traffic_average

def read_crash_times(filename):
    '''
    This function reads filename and returns pre-processed data.
 
    :param filename: input filename string
    :type filename: string

    :returns: pre-processed data for plotting
    :return type: pandas dataframe
    '''
    assert isinstance(filename,str)
    df = pd.read_csv(filename,sep = '\t', header = 1)
    df = df.drop(['Unknown', 'Unnamed: 10'], 1) # Dataframe pre-processing

    assert isinstance(df,pd.DataFrame)
    return df

def get_time_and_day(dataframe):
    '''
    This function returns data, rows and columns for a seaborn heatmap
 
    :param data: input dataframe
    :type data: pandas dataframe
    

    :returns: data ,rows, columns read to be plotted
    :return type: 3-tuple of plot variables.
    '''
    assert isinstance(dataframe,pd.DataFrame)
    rows = list(dataframe['FieldDesc'].unique())
    rows = rows[:-2]
    columns = list(dataframe.iloc[:0, 1:-1])
    data = []
    data = []
    for i in range(10):
        data.append(np.array(dataframe.iloc[i, 1:-1]))
    data = data[:-2]

    return data,rows,columns

def read_alcohol_times(filename):
    '''
    This function reads filename and returns pre-processed data.
 
    :param filename: input filename string
    :type filename: string

    :returns: pre-processed data for plotting
    :return type: pandas dataframe
    '''
    assert isinstance(filename,str)
    df = pd.read_csv(filename, sep = '\t', header = 2)
    assert isinstance(df,pd.DataFrame)
    return df

def get_alcohol_times(df):
    '''
    This function reads filename as returns pre-processed data.
 
    :param df: input data
    :type df: pandas dataframe

    :returns: seaborn variables for plotting
    :return type: 3-tuple of plot variables.
    '''
    assert isinstance(df,pd.DataFrame)
    df.head()
    rows = list(df['FieldDesc'].unique())
    rows = rows[:-2]
    total = []
    al_related = []
    total = list(df['Number2'])
    total = total[:-2]
    al_related = list(df['Alcohol--Related2'])
    al_related = al_related[:-2]

    assert isinstance(rows,list)
    assert isinstance(al_related,list)
    assert isinstance(total,list)
    return rows,al_related,total