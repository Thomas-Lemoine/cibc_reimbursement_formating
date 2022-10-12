
import pandas as pd

from settings import CSV_INPUT_FILENAME, PARSED_CSV_FILENAME
from functions import prepare_csv, ask_user_yesnomaybe

def main():
    
    df = pd.read_csv(CSV_INPUT_FILENAME, header=None)

    df = prepare_csv(df)

    #store the csv
    df.to_csv(PARSED_CSV_FILENAME)

    # ask_user_yesnomaybe()
    ask_user_yesnomaybe(df)

if __name__ == "__main__":
    main()
    
