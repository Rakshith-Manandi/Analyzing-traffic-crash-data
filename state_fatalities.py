import pandas as pd
import numpy as np

def readFile(filename):
    '''
    This function takes a CSV file and uses the read_csv attribute of pandas to return a DataFrame  

    :param fname: filename for source text
    :type fname: str

    :returns: DataFrame
    '''
    assert isinstance(filename, str)
    assert filename[-4:] == '.csv'
    output = pd.read_csv(filename)
    return output

stcodes = np.asarray(['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', \
                    'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', \
                     'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', \
                     'VA', 'WA', 'WV', 'WI', 'WY'])

stpopulation = np.asarray([4858979, 738432, 6828065, 2978204, 39144818, 5456574, 3590886, 945934, 646449, 20271272, 10214860, 1431603, 1654930, 12859995, 6619680, \
                          3123899, 2911641, 4425092, 4670724, 1329328, 6006401, 6794422, 9922576, 5489594, 2992333, 6083672, 1032949, 1896190, 2890845, \
                           1330608, 8958013, 2085109, 19795791, 10042802, 756927, 11613423, 3911338, 4028977, 12802503, 1056298, 4896146, 858469, 6600299, \
                           27469114, 2995919, 626042, 8382993, 7170351, 1844128, 5771337, 586107])

def by_state(df):
    '''
    This function takes a pandas DataFrame and returns the plot variables 

    :param df: The dataframe obtained from readFile method
    :type df: pandas DataFrame

    :returns: DataFrame
    '''
    
    states = df.groupby('STATE')
    count_by_state = np.asarray(states.YEAR.count())
    global stcodes
    return stcodes, count_by_state

def by_state_per_capita(df):
    '''
    This function takes a pandas DataFrame and returns the plot variables 

    :param df: The dataframe obtained from readFile method
    :type df: pandas DataFrame

    :returns: DataFrame
    '''
    states = df.groupby('STATE')
    count_by_state = np.asarray(states.YEAR.count())
    global stcodes, stpopulation
    acc_per_capita = count_by_state / stpopulation * 1e+5
    return stcodes, acc_per_capita
