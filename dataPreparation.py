"""
A Python module for data preparation tasks.

This module provides functionalities to preprocess and prepare data
"""

import time
#importing all the required libraries that were required for this project
#For web scraping
from bs4 import BeautifulSoup
import csv
import requests

#For data analysis
import pandas as pd
import plotly as py
import seaborn as sns
from plotly.offline import iplot
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from sklearn.model_selection import train_test_split
#!pip install psycopg2
import psycopg2
import plotly.express as px
#for accessing the config file
import yaml


class dataPreparation:
    def convert_date_columns(dataframe, date_column):
        """
        Perform operations to handle date columns in a DataFrame.

        Parameters:
        ----------
        dataframe : DataFrame
            Pandas DataFrame containing the data.
        date_column : str
            Name of the column to be converted to a datetime format.

        Returns:
        ----------
        DataFrame
            DataFrame with modified date-related columns.
        """
        dataframe = dataframe.rename(columns={date_column: 'date'})
        # Making a date conversion
        dataframe['date'] = pd.to_datetime(dataframe['date'])
        dataframe['year'] = dataframe['date'].dt.year
        dataframe['month'] = dataframe['date'].dt.month

        return dataframe
    
    def wide_to_long_form(dataframe, id_vars, value_vars, var_name, value_name):
        """
        Melt a DataFrame based on specified columns.

        Parameters:
        ----------
        dataframe : DataFrame
            Pandas DataFrame containing the data.
        id_vars : list
            Columns to be kept as identifier variables.
        value_vars : list
            Columns to be melted.
        var_name : str
            Name for the new column containing the melted column names.
        value_name : str
            Name for the new column containing the values.

        Returns:
        ----------
        DataFrame
            Melted DataFrame based on the specified parameters.
        """
        melted_data = pd.melt(dataframe, id_vars=id_vars, value_vars=value_vars,
                              var_name=var_name, value_name=value_name)
        return melted_data

