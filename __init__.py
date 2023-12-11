# importing all the required libraries that were required for this project
# For web scraping
from bs4 import BeautifulSoup
import csv
import requests
# For data analysis
import pandas as pd
import plotly as py
import seaborn as sns
from plotly.offline import iplot
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from sklearn.model_selection import train_test_split
# !pip install psycopg2
import psycopg2
import plotly.express as px
# for accessing the config file
import yaml
