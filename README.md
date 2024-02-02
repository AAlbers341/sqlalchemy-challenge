Hawaii Trip

Honolulu, Hawaii Vacation Analysis
This is an analysis of time series temperature readings from various stations. To help plan this fictional trip, a climate analysis about this area helps outline how the weather is. 

# Dependencies
## %matplotlib inline
## from matplotlib import style
## style.use('fivethirtyeight')
## import matplotlib.pyplot as plt
## import numpy as np
## import pandas as pd
## import datetime as dt

# Data
## hawaii.sqlite Database

Flask App 
Designed Flask API based app to query the analysis from above. 

# Dependencies
## import sqlalchemy
## from sqlalchemy.ext.automap import automap_base
## from sqlalchemy.orm import Session
## from sqlalchemy import create_engine, func
## import datetime as dt
## from flask import Flask, jsonify

# Documentation for Calls 

Availabe Routes:
*Precipitation Scores
/api/v1.0/precipitation

*Stations and Activity Amount
/api/v1.0/stations

*Precipitation Scores of Most Active Station
/api/v1.0/tobs

*Use routes below for 'start' date or 'start' to 'end' date
/api/v1.0/
/api/v1.0//
