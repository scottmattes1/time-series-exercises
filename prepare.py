
############################## INITIAL IMPORTS ##############################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sys
import os

home_directory_path = os.path.expanduser('~')
sys.path.append(home_directory_path +'/utils')

import wrangle_utils as wu
import explore_utils as eu
import model_utils as mu
import env

import warnings
warnings.filterwarnings("ignore")



###################### ACQUIRE SALES DATA FUNCTION ##########################

def acquire_sales_data():
    """
    Pulls in the sales data from a csv, does some cleaning and sets the date to a TimeIndex
    """
    df = pd.read_csv('sales.csv')

    #Rename sale_date to 'date'
    df = df.rename(columns={'sale_date': 'date'})
    df= df.drop(columns='Unnamed: 0')

    return df
    
    
def date_set_index(df, col):
    """
    Renames the date column to 'date' and sets it as the index of the dataframe. Returns the updated dataframe.
    """
    # Rename the designated columns 'date'
    df = df.rename(columns={col: 'date'})
    
    # Set the date as the index
    df = df.set_index('date')

    return df


###################### ACQUIRE GERMAN DAILY FUNCTION #########################

def acquire_german_daily():
    """
    Opens opsd_german_daily and normalizes the names
    """
    df = pd.read_csv('opsd_germany_daily.csv')
    df = wu.normalize_column_names(df)
    df = df.rename(columns={'wind+solar': 'wind_solar'})
    return df


###################### TIME GRAPH ALL COLUMNS FUNCTION #######################

def time_graph_all_columns(df):
    """
    Graphs all features over time
    """
    for col in df.columns:
        df.resample("M")[col].agg('mean').plot()
        plt.title(f'{col} over time')
        plt.show()


###################### ADD MONTH YEAR FUNCTION ###############################

def add_month_year(df):
    """
    Adds a month and year column. to a dataframe with a TimeIndex. Outputs the updated dataframe
    """
    # Get date values from the time index and assign it to a column called month
    df['month'] = df.index.month_name()
    
    # Get date values from the time index and assign it to a column called year
    df['year'] = df.index.year
    
    return df


###################### CHECK TIME NULLS FUNCTION #############################

def check_time_nulls(df):
    """
    Checks the time range of the data and compares it against the number of the observations
    """
    # Print the number of rows
    print('Number of rows:', df.index.nunique())
    
    # Print the number of value
    print(f'Value counts: {df.index.value_counts().value_counts()}')
    
    # Print the range between the first observation and the last observation
    n_days = timeindex.max() - df.index.min() + pd.Timedelta('1d')
    print(f"Number of days between first and last day:", n_days)
    

    
    
    
    
    
    
    
    
    
    