
import pandas as pd
import re
from datetime import datetime

from settings import REF_DATE, XLSX_RESULTS_FILENAME, CSV_RESULTS_FILENAME


def datestr_to_dateobj_in_row(row):
    # ex : 2018-12-04
    date = row["Date"]
    date = datetime.strptime(date, '%Y-%m-%d').date()
    return date

def dateobj_to_datestr_in_row(row):
    date = row["Date"]
    return date.strftime("%Y-%m-%d")


# Rename some rows
def rename_row(row):
    """
    Receive a pd.DataFrame row with a "Name" column,
    and crop the "Name" to be shorter and capture only the necessary information.
    """
    row_name = row["Name"]
    #print(f"Original : '{row_name}'")
    remove_substr_lst = ["Point de vente - ", "Interac ACHAT AU DETAIL ", "Debit Visa ACHAT AU DETAIL ", 
            "VISA ", "DEBIT ", "Operations en centre bancaire ", "Services bancaires en direct ", 
            r'\b\d{8,}\s?\b', r'\b\d{8,}\b', r'\b\d+.\d+ \w{3} @ \d+.\d+\b']

    for substr in remove_substr_lst:
        row_name = re.sub(substr, "", row_name)
            
    row_name = row_name.strip()

    if "FRAIS DE SERVICE" in row_name:
        row_name = "FRAIS DE SERVICE"

    if row_name == "":
        row_name = "Empty name"
        
    #print(f"Became  : '{row_name}'\n")
        
    return row_name


def prepare_csv(df: pd.DataFrame):

    # Naming the columns
    df.columns = ["Date", "Name", "Loss", "Gain"]
    
    # Remove the Gain column (all we care about are the rows that have a positive loss)
    df = df.drop(["Gain"], axis=1)
    # Remove the lines where there is no loss (received money, etc.)
    df.dropna(subset = ["Loss"], inplace=True)

    # Update the date format
    df['Date'] = df.apply(lambda row: datestr_to_dateobj_in_row(row), axis=1)
    
    # We only look at the rows that occured after the REF_DATE
    df = df[df['Date'] >= REF_DATE]

    # Update back the date format
    df['Date'] = df.apply(lambda row: dateobj_to_datestr_in_row(row), axis=1)
    
    #crop the row names
    df['Name'] = df.apply (rename_row, axis=1)
    
    df.reset_index(drop=True, inplace=True)

    return df


def ask_user_yesnomaybe(df: pd.DataFrame):
    answers_lst = []
    reasons_lst = []
    for _, row in df.iterrows():
        ans = input(f"Is a refund needed for {row['Date']}, {row['Name']}, {row['Loss']:.2f}$?\n")
        reason = input(f"Please give an optional short explanation of your choice:\n")
        reasons_lst.append(reason)
        if ans.startswith("y"):
            answers_lst.append("Yes")
        elif ans.startswith("n"):
            answers_lst.append("No")
        else:
            answers_lst.append("Maybe")
    df["Answer"] = answers_lst
    df["Reason"] = reasons_lst
    df.to_excel(XLSX_RESULTS_FILENAME)
    df.to_csv(CSV_RESULTS_FILENAME)

    
        
    
    

"""def ask_user_yesnomaybe(df):
    total_yes, total_maybe, total_no = 0,0,0
    yes_str, no_str, maybe_str="","",""
    with open(RESULTS_FILENAME, "w") as output_file:
        for _, row in df.iterrows():
            ans = input(f"Is a refund needed for {row['Date']}, {row['Name']}, {row['Loss']:.2f}?\n")
            info_str = f"{row['Date']}\t{row['Name']}\t{row['Loss']}\n"

            if ans[0] == "y":
                print("Added to Yes")
                total_yes += row["Loss"]
                yes_str +=   f"Yes   : {info_str}"
            elif ans[0] == "n":
                print("Added to No")
                total_no += row["Loss"]
                no_str +=    f"No    : {info_str}"
            else:
                print("Added to Maybe")
                total_maybe += row["Loss"]
                maybe_str += f"Maybe : {info_str}"

        output_file.write(f"YES : \nTOTAL of YES: {total_yes}\n{yes_str}\n\n")
        output_file.write(f"MAYBE : \nTOTAL of MAYBE: {total_maybe}\n{maybe_str}\n\n")
        output_file.write(f"NO : \nTOTAL of NO: {total_no}\n{no_str}\n\n")
    print(f"{total_yes   =}")
    print(f"{total_maybe =}")
    print(f"{total_no    =}")"""