'''Unit tests for the increment() and addy_split() functions in helper_functions.py'''

import pandas as pd
from lambdata.helper_functions import increment, addy_split

# write a funciton to test increment()
def test_increment_int():
    # write assert statements inside of the testing function
    assert increment(3) == 4
    # assert helper_functions.increment(3) == 5

def test_increment_float():
    # write assert statements inside of the testing function
    assert increment(2.5) == 3.5

def test_increment_neg_int():
    # write assert statements inside of the testing function
    assert increment(-10) == -9

def test_increment_neg_float():
    # write assert statements inside of the testing function
    assert increment(-5.5) == -4.5

# Code to test the addy_split() function
ADDRESS1 = '0848 Tina Lodge\nWest Tiffanyland, RI 09506'
ADDRESS2 = '19163 Amber Courts\nJamiebury, NH 65040'

df = pd.DataFrame({'address': [ADDRESS1, ADDRESS2]})

def test_addy_split():
    '''test if addy_split can successfully break apart addresses
    after the newline character. Should work with cities with multiple word names
    as well as cities with single word names'''
    assert addy_split(df['address']).shape == (2,3)
    assert addy_split(df['address']).columns.to_list() == ['city', 'state', 'zip']
    assert addy_split(df['address'])['city'].to_list() == ['West Tiffanyland', 'Jamiebury']
    assert addy_split(df['address'])['state'].to_list() == ['RI', 'NH']
    assert addy_split(df['address'])['zip'].to_list() == ['09506', '65040']    