import re
import pandas as pd
import numpy as np
from faker import Faker
# from us import states as states_pkg

fake = Faker()

test_df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
test_addy_df = pd.DataFrame([{"address": fake.address()} for x in range(50)])


def increment(num):
    '''increment a number by one'''
    return num + 1


def null_count(df):
    """Check a dataframe for nulls and return the number of missing values"""
    return df.isnull().sum().sum()


def train_test_split(df, frac=0.8):
    """
    Create a Train/test split function for a dataframe and returns both the
    training and testing sets
    """
    train = df.sample(frac=frac)
    test = df.drop(train.index).sample(frac=1.0)
    return train, test


def randomize(df, seed):
    """"
    Develop a randomization function that randomizes all of a dataframes cells
    then returns that randomized dataframe
    """
    randomized_df = df.sample(frac=1.0, random_state=seed)
    return randomized_df

def addy_split(addy_series):
    """
    Split addresses into three columns (df['city], df['state'], and df['zip']).
    You can use regexes to detect the format and pull out important pieces.
    """

    addy_series = addy_series.str.split("\n", n=1, expand=True)[1]

    df = pd.DataFrame()
    city_list = []
    state_list = []
    zip_list = []

    for addy in addy_series:
        city_list.append(addy.split(',')[0])
        state_list.append(addy.split(',')[1].split()[0])
        zip_list.append(addy.split(',')[1].split()[1])

    df['city'] = city_list
    df['state'] = state_list
    df['zip'] = zip_list
    
    return df


def abbr_2_st(state_series, abbr_2_st=True):
    """
    Return a new column with the full name from a State abbreviation column
    -> An input of FL would return Florida.
    """
    st_list = states_pkg.STATES  # states if you want to do it the list way
    st_abbr_list = [state.abbr for state in st_list]  # abbreviations list

    df = pd.DataFrame()
    translated = []

    if abbr_2_st:
        col_title = 'abbr_2_st'
        for state in state_series:
            translated.append(states_pkg.lookup(state).name)
    else:
        col_title = 'st_2_abbr'
        for state in state_series:
            translated.append(states_pkg.lookup(state).abbr)

    df[col_title] = translated

    return df


def list_2_series(list_2_series, df):
    """
    Single function to take a list and dataframe, turn it into a series and add it to a
    dataframe as a new column
    """
    temp_df = pd.DataFrame()
    temp_df['list'] = list_2_series
    new_df = pd.concat([df, temp_df], axis=1)
    return new_df


def rm_outlier(df):
    """
    A 1.5*Interquartile range outlier detection/removal function that gets
    rid of outlying rows and returns that outlier cleaned dataframe.
    """
    cleaned_df = pd.DataFrame()

    for (columnName, columnData) in df.iteritems():
        Q1 = columnData.quantile(0.25)
        Q3 = columnData.quantile(0.75)
        IQR = Q3 - Q1
        lower_fence = Q1 - 1.5 * IQR
        upper_fence = Q3 + 1.5 * IQR
        mask = columnData.between(lower_fence, upper_fence, inclusive=True)
        cleaned = columnData.loc[mask]
        cleaned_df[columnName] = cleaned

    return cleaned_df
    # cleaned_df = pd.DataFrame()

    # for (columnName, columnData) in df.iteritems():
    #     Q1 = columnData.quantile(0.25)
    #     Q3 = columnData.quantile(0.75)
    #     mask = columnData.between(Q1, Q3, inclusive=True)
    #     IQR = columnData.loc[mask]
    #     cleaned_df[columnName] = IQR

    # return cleaned_df


def split_dates(date_series):
    """
    Function to split dates of format "MM/DD/YYYY" into multiple columns
    (df['month'], df['day'], df['year']) and then return the same dataframe
    with those additional columns
    """
    df = pd.DataFrame()
    month_list = []
    day_list = []
    year_list = []
    expression = r'([0-9]{2})[\/]{1}([0-9]{2})[\/]{1}([0-9]{4})'

    for date in date_series:
        date_match = re.match(expression, date)
        if date_match:
            month_list.append(date_match.group(1))
            day_list.append(date_match.group(2))
            year_list.append(date_match.group(3))

    df['month'] = month_list
    df['day'] = day_list
    df['year'] = year_list

    return df

# TODO - Figure out how to implement a test for student ideas, make stretch goal maybe?
