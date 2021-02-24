# -------------------------------------------------------
# Selection of small data cleaning/integration functions
# for records in .csv format
# Examples used here applied to dirty health records
# by Ewen Bramble
# -------------------------------------------------------

import pandas as pd

def load_data():
    """Function asks user to input path and filename of csv and returns a pandas data"""

    while True:
        try:
            csv = input("Please enter path/filename of csv: ")
            df = pd.read_csv(csv)
            break
        except:
            "Path/filename not found"

    return df

def null_take_recent():
    """Function to integrate a merged dataset csv file (eg inner join)
    where you have duplicate attributes (eg x_email, y_email) and need to resolve
    missing or different values. Timestamp used to take most recent value if not-null"""

    ####
    # Currently set up to process 'email' attributes.
    ####

    import datetime
    df = load_data()

    out_list = []
    for row in df.itertuples():
        # Change timestamp attribute names/format here
        x_date = datetime.datetime.strptime(row.employment_timestamp[:10], '%Y-%m-%d')
        y_date = datetime.datetime.strptime(row.consultation_timestamp[:10], '%Y-%m-%d')
        # check for null value in x, if null assign y
        if row.email_x == "":
            out_list.append(row.email_y)
        # check for null value in y, if null assign x
        elif row.email_y == "":
            out_list.append(row.email_x)
        # otherwise, take the most recent
        else:
            if x_date > y_date:
                out_list.append(row.email_x)
            else:
                out_list.append(row.email_y)
    df['email'] = out_list # single merged attribute from x and y versions

def gender_resolve():
    """Resolves questionably-labelled/missing gender attributes in a csv record
    using the gender-guesser module (uses underlying data from the
    program “gender” by Jorg Michael"""

    import gender_guesser.detector as gender

    df = load_data()

    d = gender.Detector(case_sensitive=False) # Gender guesser object

    records_changed = [] # List of affected records by index

    for i in range(len(df)):
        if d.get_gender(df['first_name'][i]) == 'unknown': # If unknown/missing first name, take gender of middle name
            if d.get_gender(df['middle_name'][i]) == 'male' and df['gender'][i] != 'm':
                df.at[i, 'gender'] = 'm'
                records_changed.append(i)
            elif d.get_gender(df['middle_name'][i]) == 'female' and df['gender'][i] != 'f':
                df.at[i, 'gender'] = 'f'
                records_changed.append(i)
            else:
                pass
        elif d.get_gender(df['first_name'][i]) == 'male' and df['gender'][i] != 'm':
            df.at[i, 'gender'] = 'm'
            records_changed.append(i)
        elif d.get_gender(df['first_name'][i]) == 'female' and df['gender'][i] != 'f':
            df.at[i, 'gender'] = 'f'
            records_changed.append(i)

    print("Indexes of changed records: {}".format(records_changed))
    print("Total number of records changed: {}".format(len(records_changed)))

def impute_average():
    """Function to calculate the average salary per listed occupation
    and impute where missing in csv record"""
    # Assumes column names 'occupation' and 'salary'

    df = load_data()

    salaries = dict() # Dictionary with occupation as keys and salaries as values
    occ_count = dict() # Dictionary with counts for each occupation occurrence in dataset

    for i in range(len(df)):
        if pd.notnull(df.occupation[i]): # First check if occupation listed in record
            if df.occupation[i] not in salaries:
                if pd.notnull(df.salary[i]) and df.salary[i] >= 0: # Check salary not null or negative
                    salaries[df.occupation[i]] = df.salary[i] # If not null, add first occupation/salary instance
                    occ_count[df.occupation[i]] = 1 # Add count for occupation
                else:
                    pass
            else:
                if pd.notnull(df.salary[i]) and df.salary[i] > 0: # If salary valid
                    salaries[df.occupation[i]] += (df.salary[i]) # Add subsequent instances to divtionary
                    occ_count[df.occupation[i]] += 1

    average_salary = dict() # Dictionary for average salary per occupation
    for key, value in salaries.items():
        average_salary[key] = (value / occ_count[key])

    # Now impute salaries where missing
    for i in range(len(df)):
        if pd.isnull(df.occupation[i]): # If no occupation, do nothing - cannot add avg salary
            pass
        elif pd.isnull(df.salary[i]) or df.salary[i] <= 0: # If salary missing/0/negative, impute average
            df.at[i, 'salary'] = average_salary[df.occupation[i]]




