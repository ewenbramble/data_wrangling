# Code was written for a project involving profiling/cleaning a dirty health record dataset
# by Ewen Bramble

import pandas as pd

def weight_validity(min = 0, max = 500):
    """Function takes a health database in csv format and prints validity of weight records
    :param min: Minimum allowed weight in kg, default 0
    :param max: Maximum allowed weight in kg, default 500"""

    # Get csv path/filename
    while True:
        try:
            csv = input("Please enter path/filename of csv: ")
            df = pd.read_csv(csv)
            break
        except:
            "Path/filename not found"
    
    w_count = 0
    w_invalid_count = 0
    
    for item in df['weight']: # Name of column containing weight records
        w_count += 1
        if item <= min or item > max:
            w_invalid_count += 1

    w_validity = ((w_count - w_invalid_count)/w_count) * 100
    print("Total count: {}".format(w_count))
    print("Invalid count: {}".format(w_invalid_count))
    print("Weight validity %: {}".format(w_validity))


if __name__ == '__main__':
    weight_validity()