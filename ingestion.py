import pandas as pd
import numpy as np
import os
import json
from datetime import datetime




#############Load config.json and get input and output paths
with open('config.json','r') as f:
    config = json.load(f) 

input_folder_path = config['input_folder_path']
output_folder_path = config['output_folder_path']



#############Function for data ingestion
def merge_multiple_dataframe():
    #check for datasets, compile them together, and write to an output file
    current_path = os.getcwd()

    all_files = []
    filenames = os.listdir(input_folder_path)
    for filename in filenames:

        if filename.endswith(".csv"):
            all_files.append(os.path.join(current_path, input_folder_path, filename))

    df = pd.DataFrame(
        columns=[
            "corporation",
            "lastmonth_activity",
            "lastyear_activity",
            "number_of_employees",
            "exited",
        ]
    )

    for file in all_files:
        df_temp = pd.read_csv(file)
        df = pd.concat([df, df_temp])

    # Remove duplicates
    cleaned_df = df.drop_duplicates()

    cleaned_df.to_csv("%s/finaldata.csv" % output_folder_path, index=False)

    with open(os.path.join(output_folder_path, "ingestedfiles.txt"), "w") as report_file:
        for line in filenames:
            report_file.write(line + "\n")


if __name__ == '__main__':
    merge_multiple_dataframe()
