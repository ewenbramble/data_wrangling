# Code was written for a project involving profiling/cleaning a dirty health record dataset
# by Ewen Bramble

import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta

def age_consistency():
    """Function compares patient birthdate with consult timestamp in csv database
    and checks the consistency of patient age-at-consult"""

    # Get csv path/filename
    while True:
        try:
            csv = input("Please enter path/filename of csv: ")
            df = pd.read_csv(csv)
            break
        except:
            "Path/filename not found"

    records_checked = 0 # Count records
    match = 0 # Correct records will match age in years, diff between birthdate and timestamp

    for i in range(len(df)):
        records_checked += 1
        # Change column names and date formats over next 4 lines as required
        bd_datetime = datetime.datetime.strptime(df['birth_date'][i], '%d/%m/%Y')
        timestamp_datetime = datetime.datetime.strptime(df['consultation_timestamp'][i][:10], '%Y-%m-%d')
        calculated_age = relativedelta(timestamp_datetime, bd_datetime).years
        if int(df['age_at_consultation'][i]) == calculated_age:
            match += 1
        else:
            pass
    consistency = float(match/records_checked) * 100
    print("Records checked: {}".format(records_checked))
    print("Matches: {}".format(match))
    print("Consistency: {}".format(consistency))