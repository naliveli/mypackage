"""
Exploratory Data Analysis (EDA) Python Script

Description:
This Python script is dedicated to conducting Exploratory Data Analysis (EDA) on a dataset. 
The purpose of this script is to explore, visualize, and gain insights into the dataset 
before performing further data processing, feature engineering, or modeling tasks.

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

class analysis:
    def plot_feature_distribution(dataframe, feature):

        """
        Plots the distribution of a specified feature in a DataFrame using a histogram.

        Parameters:
        dataframe (DataFrame): The pandas DataFrame containing the dataset.
        feature (str): The name of the feature/column whose distribution is to be plotted.

        Returns:
        None: Displays the histogram plot of the specified feature's distribution.
        """
        dataframe[feature].hist()
        plt.xlabel(f'{feature.capitalize()}')
        plt.ylabel('Frequency')
        plt.title(f'Distribution of {feature}')
        plt.show()
        
    def plot_bar_chart(dataframe, title='', xlabel='', ylabel='', figsize=(10, 6)):
        """
        Plots a bar chart for a specified feature in a DataFrame.

        Parameters:
        dataframe (DataFrame): The pandas DataFrame containing the dataset.
        title (str, optional): Title of the bar chart (default is '').
        xlabel (str, optional): Label for the x-axis (default is '').
        ylabel (str, optional): Label for the y-axis (default is '').
        figsize (tuple, optional): Size of the figure (default is (10, 6)).

        Returns:
        None: Displays the bar chart for the specified feature.
        """
        dataframe.plot(kind='bar', title=title, ylabel=ylabel, xlabel=xlabel, figsize=figsize)
        plt.show() 
        
    def plot_box_chart(dataframe, feature, title='', xlabel='', ylabel='', figsize=(10, 6)):
        """
        Plots a box plot for a specified feature in a DataFrame.

        Parameters:
        dataframe (DataFrame): The pandas DataFrame containing the dataset.
        feature (str): The name of the feature/column for which the box plot is to be plotted.
        title (str, optional): Title of the box plot (default is '').
        xlabel (str, optional): Label for the x-axis (default is '').
        ylabel (str, optional): Label for the y-axis (default is '').
        figsize (tuple, optional): Size of the figure (default is (10, 6)).

        Returns:
        None: Displays the box plot for the specified feature.
        """
        dataframe[feature].plot(kind='box', title=title, ylabel=ylabel, xlabel=xlabel, figsize=figsize)
        plt.show()
    
        
     