
from re import U
import pandas as pd

from settings import *
from functions import prepare_csv, ask_user_yesnomaybe

def main():
    
    df = pd.read_csv(CSV_INPUT_FILENAME, header=None)

    df = prepare_csv(df)

    #store the csv
    df.to_csv(PARSED_CSV_FILENAME)

    # ask_user_yesnomaybe()
    ask_user_yesnomaybe(df)

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    main()
    