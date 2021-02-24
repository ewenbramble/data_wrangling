# Code was written for a project involving profiling/cleaning a dirty health record dataset
# by Ewen Bramble

import pandas as pd
import re

def email_validity():
    """Function takes a health database in csv format and prints validity of email records"""

    # Get csv file/pathname
    while True:
        try:
            csv = input("Please enter path/filename of csv: ")
            df = pd.read_csv(csv)
            break
        except:
            "Path/filename not found"

    count = 0 # Total number records
    invalid_count = 0

    regex = '[^@]+@[^@]+\.[^@]+' # Email address must contain @ followed by .

    for item in df['email']: # Name of column containing email records
        if isinstance(item, str):
            if (re.search(regex, item)):
                count += 1
            else:
                count += 1
                invalid_count += 1
        else:
            pass

    validity = ((count - invalid_count)/count) * 100
    print("Total count: {}".format(count))
    print("Invalid count: {}".format(invalid_count))
    print("Email validity: {}".format(validity))


if __name__ == '__main__':
    email_validity()