# Code was written for a project involving profiling/cleaning a dirty health record dataset
# by Ewen Bramble

import pandas as pd

def calculate_benfords():
    """Function prints Benford's distribution of a numeric column in a csv file"""

    # Get path/name of csv
    while True:
        try:
            csv = input("Please enter path/filename of csv: ")
            df = pd.read_csv(csv)
            break
        except:
            "Path/filename not found"

    # Get name of attribute
    while True:
        try:
            attribute = input("Please enter column name to check Benford's distribution: ")
            if attribute in df.columns:
                break
        except:
            "Invalid column name"

    records = 0 # Count total records
    count_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0} # Dictionary to count first digit each record
    for item in df[attribute]:
        records += 1
        if str(item)[0] == '0':
            count_dict[0] += 1
        elif str(item)[0] == '1':
            count_dict[1] += 1
        elif str(item)[0] == '2':
            count_dict[2] += 1
        elif str(item)[0] == '3':
            count_dict[3] += 1
        elif str(item)[0] == '4':
            count_dict[4] += 1
        elif str(item)[0] == '5':
            count_dict[5] += 1
        elif str(item)[0] == '6':
            count_dict[6] += 1
        elif str(item)[0] == '7':
            count_dict[7] += 1
        elif str(item)[0] == '8':
            count_dict[8] += 1
        elif str(item)[0] == '9':
            count_dict[9] += 1

    print(count_dict)
    distribution = dict()

    for k,v in count_dict.items():
        distribution[k] = (v/records)*100
    print(distribution)

if __name__ == '__main__':
    calculate_benfords()