"""
Data Extraction Python Script

Description:
This Python script is dedicated to scrape the data from the website, connect to the postgres server and create database and table to store the scraped data

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

class dataHandler:
    def fetch_db_redentials():
        """This function will fetch the login username and password for the postgres server from the config.yaml file"""
        try:
            with open('C:\\Users\\User\\Downloads\\gunCultureAnalysisUSA\\config.yaml', 'r') as file:
                config = yaml.safe_load(file)
                # Access values from the config and getting the username and password for the database
                db_username = config['Database']['username']
                db_password = config['Database']['password']
                print("Successfully retrieved database credentials from the config.yaml file")
            return db_username,db_password
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def create_db_postgres(db_username,db_password):
        """This function will connect to postgres server and create databse and table to store the scraped data from the website."""
        try:
        #Establishing the connection to the postgres database server
            connection = psycopg2.connect(
               database="postgres", user=db_username, password=db_password
            )
            connection.autocommit = True
            #Creating a cursor object using the cursor() method
            cursor = connection.cursor()
            print("Database creation started")
            #SQL query to check the if any database exists with the same name that we have given, If so we will drop that databse 
            check_db='''DROP DATABASE IF EXISTS crime_data_db'''
            #SQL query to create a databse
            sql = '''CREATE database crime_data_db''';
            #executing the query
            cursor.execute(check_db)
            #commiting the changes to the databse
            connection.commit()
            cursor.execute(sql)
            connection.commit()
            print("Database created successfully........")
            connection.close()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    def create_table_postgres(db_username,db_password):
        """This function will connect to postgres server and create databse and table to store the scraped data from the website."""
        try:
            connection = psycopg2.connect(
               database="crime_data_db", user=db_username, password=db_password
            )
            connection.autocommit = True
            #Creating a cursor object using the cursor() method
            cursor = connection.cursor()
            print("Database creation started")
            print("Table creation started")
            #Table creation
            #SQL query to check the if any table exists with the same name that we have given, If so we will drop that table 
            check_tb='''DROP TABLE IF EXISTS crime_data'''
            #SQL query to create a table
            table ='''create table crime_data (incident_date DATE,state varchar(100),city varchar(100),n_killed int,n_injured int)'''
            #executing the query
            cursor.execute(check_tb)
            #commiting the changes to the databse
            connection.commit()
            cursor.execute(table)
            connection.commit()
            #Closing the connection
            connection.close()
            print("Table Created Successfully")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None 

    def fetch_data_from_github_repo(github_url):
        """This function fetches the data from the githihub by taking input parameter as data file github url."""
        try:
            nics_data = pandas.read_csv(github_url)
            print("Data fetched from Github repository successfully")
            return nics_data
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    def scrape_data(soup):
        """This function will scrape the data from the website"""
        table = soup.find("table")
        # Loop through the collected site data and extract the information needed
        for row in table.findAll('tr')[1:]:
            col = row.find_all('td')
            date = col[1].string
            state = col[2].string
            city = col[3].string
            killed = col[5].string
            injured = col[6].string
            connection = psycopg2.connect(database="crime_data_db", user='postgres', password='Yeshiva5076')
            cursor = connection.cursor()
            #Inserting the data into the databse table 
            data_insert="""insert into crime_data values('"""+date+"""','"""+state+"""','"""+city+"""','"""+str(killed)+"""','"""+str(injured)+"""')"""
            #executing the query
            cursor.execute(data_insert)
            #commiting the changes to the database after inserting the data
            connection.commit()
            #closing the connection
            connection.close()
    def fetch_data_from_postgres(db_username,db_password):        
            #Establishing the connection to the postgres database server
            connection = psycopg2.connect(
               database="crime_data_db", user=db_username, password=db_password
            )
            cursor = connection.cursor()
            #executing the query to fecth the data from the table that we credted in the postgres server database
            cursor.execute('''SELECT * from crime_data''')
            #creating a dataframe 
            crime_data = pd.DataFrame(cursor.fetchall(),columns=['date','state','city','n_killed','n_injured'])
            #closing the connecting to the postgres server database after fetching the data from the postgres server database
            connection.close()
            return crime_data 
    