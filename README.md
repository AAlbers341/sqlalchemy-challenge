# Hawaii Trip - Vacation Analysis

This project analyzes time series temperature readings from various stations in Honolulu, Hawaii. The goal is to provide valuable insights into the climate to help plan a fictional trip to this area.

## Dependencies

- `%matplotlib inline`
- `from matplotlib import style`
- `style.use('fivethirtyeight')`
- `import matplotlib.pyplot as plt`
- `import numpy as np`
- `import pandas as pd`
- `import datetime as dt`

## Data

### hawaii.sqlite Database

The analysis is based on data stored in the `hawaii.sqlite` database.

## Flask App

A Flask API-based app has been designed to query the analysis results obtained above.

### Dependencies

- `import sqlalchemy`
- `from sqlalchemy.ext.automap import automap_base`
- `from sqlalchemy.orm import Session`
- `from sqlalchemy import create_engine, func`
- `import datetime as dt`
- `from flask import Flask, jsonify`

## Documentation for API Calls

### Available Routes:

1. Precipitation Scores:
   - Endpoint: `/api/v1.0/precipitation`

2. Stations and Activity Amount:
   - Endpoint: `/api/v1.0/stations`

3. Precipitation Scores of the Most Active Station:
   - Endpoint: `/api/v1.0/tobs`

4. Use the routes below for 'start' date or 'start' to 'end' date:

   - Endpoint: `/api/v1.0/<start>`
   - Endpoint: `/api/v1.0/<start>/<end>`

Replace `<start>` and `<end>` with the desired date parameters.
