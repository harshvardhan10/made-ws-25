import pandas as pd
import os


def extract_csv_from_url(url):
    """
    Extracts a csv file from a url and returns a pandas dataframe
    """
    df = pd.read_csv(url)
    return df


def preprocess_flood_data(flood_df):
    """
    Preprocesses the flood data
    """
    # Drop unnecessary columns
    flood_df = flood_df.drop(columns=[
        'Unnamed: 0', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
        'datetime'
    ])

    # Fill missing values and drop where necessary
    flood_df = flood_df.dropna(subset=['ID', 'Year', 'Month'])
    flood_df[['Day', 'Duration (days)', 'fatality', 'Severity', 'Cause']] = flood_df[
        ['Day', 'Duration (days)', 'fatality', 'Severity', 'Cause']].fillna(-1)
    flood_df[['Lat ', 'Long']] = flood_df[['Lat ', 'Long']].fillna(1000)

    # Drop row with ID 834 as the data does not match the rest of the dataset
    flood_df = flood_df[flood_df['ID'] != 834]

    # Assign suitable data types
    flood_df[['ID', 'Year', 'Month', 'Day', 'Duration (days)', 'fatality', 'Country code', 'Continent Code']] = \
        flood_df[
            ['ID', 'Year', 'Month', 'Day', 'Duration (days)', 'fatality', 'Country code', 'Continent Code']].astype(
            int)
    flood_df[['Severity', 'Lat ', 'Long']] = flood_df[['Severity', 'Lat ', 'Long']].astype(float)

    # Format column names
    flood_df.columns = flood_df.columns.str.lower().str.strip()

    flood_df = flood_df.sort_values('id')
    flood_df.reset_index(drop=True, inplace=True)
    return flood_df


if __name__ == "__main__":
    flood_data_url = "https://zenodo.org/records/7545697/files/cyberFlood_1104.csv?download=1"
    hpi_data_url = "https://www.fhfa.gov/hpi/download/monthly/hpi_master.csv"

    flood_df = extract_csv_from_url(flood_data_url)
    flood_df = preprocess_flood_data(flood_df)

    hpi_df = extract_csv_from_url(hpi_data_url)
    # hpi dataset is already clean so no need to preprocess

    flood_df.to_csv('../data/flood.csv', index=False)
    hpi_df.to_csv('../data/hpi.csv', index=False)

