# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt



from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route('/')
def index():
    return  (
        f"Welcome to the Climate App!<br/>"
        f"<br/>"
        f"Availabe Routes:<br/>"
        f"*Precipitation Scores<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"*Stations and Activity Amount<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"*Precipitation Scores of Most Active Station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"*Use routes below for 'start' date or 'start' to 'end' date<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    """Fetch results from precipitation analysis for the past months of data"""

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # From most recent date substract in datetime format 365 to view 12 month prcp
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    data = []
    twelve_month_precip = session.query(measurement.date, measurement.prcp).filter(measurement.date >= query_date).all()

    # Append to list of dictionaries 
    for date, avg_prcp in twelve_month_precip:
        data.append({"date": date, "average_prcp": avg_prcp})

    # Return results in JSON format
    return jsonify(data)

# Close session with DB
session.close()
    
@app.route("/api/v1.0/stations")
def stations():
    """Fetch a list of stations from the dataset"""

    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Perform a query to retrieve grouped by stations and number of activity
    active_stations = session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station) \
                .order_by(func.count(measurement.station).desc()).all()
    
    # Append to list of dictionaries
    stations = []
    for station, activity in active_stations:
        stations.append({"station":station, "activity": activity})

    # Return results in JSON format
    return jsonify(stations)

# Close session with DB
session.close()

@app.route("/api/v1.0/tobs")
def most_active_station():
    """Fetch dates and temperatures observations of the most-active station from previous year of data"""

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve grouped by stations and number of activity
    active_stations = session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station) \
                .order_by(func.count(measurement.station).desc()).all()

    # Parse out most active station
    most_active = active_stations[0][0]

    # Set params for observations for previous year, 2016
    query_date_end = dt.date(2016, 12, 31)
    query_date_start = dt.date(2016, 1, 1)

    # Filter query for params and active station id
    prvs_year = []
    prvs_year_temp = session.query(measurement.date, measurement.tobs) \
        .filter(measurement.date >= query_date_start) \
        .filter(measurement.date <= query_date_end) \
        .filter(measurement.station == most_active) \
        .all()
    
    # Append to list of dictionaries
    for date, tobs in prvs_year_temp:
        prvs_year.append({"station": most_active, "date": date, "temp":tobs})

    # Return results in JSON format
    return jsonify(prvs_year)

# Close session with DB
session.close()

@app.route("/api/v1.0/<start>")
def temperature_stats_start(start):
    """Calculate TMIN, TAVG, and TMAX for dates greater than or equal to the start date"""

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Convert the start date string to a datetime object
    start_date = dt.datetime.strptime(start, "%Y-%m-%d").date()

    # Query for temperature statistics
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)) \
        .filter(measurement.date >= start_date) \
        .all()

    # Convert the result to a dictionary
    temperature_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    # Return results in JSON format
    return jsonify(temperature_stats)

# Close session with DB
session.close()

@app.route("/api/v1.0/<start>/<end>")
def temperature_stats_start_end(start, end):
    """Calculate TMIN, TAVG, and TMAX for dates between the start and end dates"""

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Convert the start and end date strings to datetime objects
    start_date = dt.datetime.strptime(start, "%Y-%m-%d").date()
    end_date = dt.datetime.strptime(end, "%Y-%m-%d").date()

    # Query for temperature statistics
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)) \
        .filter(measurement.date >= start_date) \
        .filter(measurement.date <= end_date) \
        .all()

    # Convert the result to a dictionary
    temperature_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    # Return results in JSON format
    return jsonify(temperature_stats)

# Close session with DB
session.close()

if __name__ == "__main__":
    app.run(debug=True)